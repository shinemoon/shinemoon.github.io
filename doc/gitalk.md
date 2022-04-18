因为当前（至少NexT主题自带下）的gitalk使用md5(post_path)作为label，从而导致了「WIKI中的评论初始化」无法正常使用。我这边用bash重写了自动生成issue的代码，顺便为了保证自动化增加了issue是否存在的判定以及github actions的支持。

bash代码如下

---

username="C0MM4ND" # github username
token="XXXXXX"  # personal access token
repo_name="c0mm4nd.com" # issues repo
host="https://c0mm4nd.com" # host url without suffix /
sitemap_path="/sitemap.xml" # sitemap path
post_regex="https://c0mm4nd.com/post/[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*" # !important, you have to distinguish the posts,
                                                                     # or the tags, categories even indexs will pollute 
                                                                     # your github issue
kind="Gitalk"

# return $title
read_title () {
    post_url=$1
    title=$(curl -s $post_url | grep -oP '(?<=<title>)(.*)(?=</title>)')
}

# return $post_path
get_post_path () {
    full_post_url=$1
    post_path=${full_post_url#"$host"} # cut host prefix
}

# return $exist
check_issue_exist () {
    post_url=$1
    post_title=$2
    get_post_path $post_url
    hex_md5=$(echo -n $post_path | md5sum | awk '{ print $1 }')

    body=$(curl -X GET -u $username:$token -H "Accept: application/vnd.github.v3+json" -H "Content-Type: application/json" \
    "https://api.github.com/repos/$username/$repo_name/issues?labels=$hex_md5")
    if [[ $body == *$post_title* ]]; then
        exist=1 # exist
    else
        exist=0
    fi
}

create_issue () {
    post_url=$1
    post_title=$2
    get_post_path $post_url
    hex_md5=$(echo -n $post_path | md5sum | awk '{ print $1 }')

    curl -X POST -u $username:$token -H "Accept: application/vnd.github.v3+json" -H "Content-Type: application/json" \
    -d "{\"body\": \"$post_url\", \"labels\": [\"$kind\", \"$hex_md5\"], \"title\": \"$post_title\" }" \
    "https://api.github.com/repos/$username/$repo_name/issues"
}


i=1
for url in $(curl -s $host$sitemap_path | grep -oP '(?<=<loc>).*?(?=</loc>)')
do
    if [[ $url =~ $post_regex ]]; then 
        echo $url" is valid post"
        read_title $url
        echo $title
        check_issue_exist $url "$title"
        if !(($exist)); then
            echo "cannot find the issue, start creating"
            create_issue $url "$title"
        fi
        i=$(($i+1))
        if !(($i % 10)); then
            sleep 2s
        fi
    fi
done

---
github actions及部署方式见此
https://github.com/C0MM4ND/scripts/tree/main/AutoIssue

技术不精没怎么写过bash，完全是为了github actions能快速启动执行才选的，请大佬们轻喷。

希望能帮到有同样需求的人。
