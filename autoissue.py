# -*- coding: utf-8 -*-  
# coding: utf-8
# Script to scan and generate gitalk comment automatically.
import os
import subprocess
import datetime
import re
import requests
import json
import time
import sys

#========= Global Config
# Post folder
pFolder = ""
rootDomain=""
# GitRelated
token = ""
repo_name=""
user=""

#=======================================================
# To list all posts in _posts folder, and just focusing 
# in newer files later that last round scanning.
#   - input: folder_path
#   - output: 'link label title'
#=======================================================
def checkPostFolder(fList, postFolder):
    # Handling the Post
    files = os.listdir(postFolder)
    # Pick newer files
    for f in files:
        # Cmp the timestamp
        res = parseFile(postFolder +'/'+f)
        if res[0]:
            fList.append("%s /%s %s"%(res[3],res[1][:48], res[2].strip()))

#=======================================================
# Parse File
# - return will be the issue's name/label/origin-link to 
#   be used for issue creation 
#   e.g. in current design, it will parse first 30 lines
#   for title, if not got ,then skip
#   - input: file_path
#   - output: [IF_VALID_FILE, label, title, link]
#=======================================================
def parseFile(filepath):
    global rootDomain 
    # need to fetch label + title from post
    lines = []
    try:
        count = 0
        with open(filepath) as openfileobject:
            for line in openfileobject:
                count = count + 1 
                if(count >= 30):
                    break
                else:
                    cv = line.strip()
                    # is it hit title?
                    tre = re.match(r"title:(.*)", cv)
                    lre = re.match(r".*/\d+-\d+-\d+-(.*)\.md",filepath)
                    if tre and lre:
                        # Title hit
                        title = tre.group(1)
                        # to fetch label - can be customized 
                        label = lre.group(1)
                        # link
                        link = rootDomain+label
                        # for title/label judge
                        if(title=='' or label==''):
                            pass
                        else:
                            return [True, label, title , link]
                    else:
                        pass
            # Not valid post, jump out
            return [False, None, None, None]
    except:
        return [False, None, None, None]

#=======================================================
# Parse Config File from config.ini
#   - input: file_path
#   - output: True/False
#=======================================================

def fetchConfig(filepath):
    try:
        with open(filepath) as openfileobject:
            for line in openfileobject:
                cv = line.strip()
                tre = re.match(r"token:(.*)", cv)
                fre = re.match(r"pFolder:(.*)", cv)
                rre = re.match(r"rootDomain:(.*)", cv)
                rpre = re.match(r"repo_name:(.*)", cv)
                ure = re.match(r"user:(.*)", cv)
                if tre:
                    token = tre.group(1)
                elif fre:
                    pFolder = fre.group(1)
                elif rre:
                    rootDomain = rre.group(1)
                elif rpre:
                    repo_name = rpre.group(1)
                elif ure:
                    user=ure.group(1)
                else:
                    print("Failed!")
                    return [None, None, None, None, None]
    else:
        # if it's in github action, then use secret
        with open('config.ini.template') as openfileobject:
            for line in openfileobject:
                cv = line.strip()
                fre = re.match(r"pFolder:(.*)", cv)
                rre = re.match(r"rootDomain:(.*)", cv)
                rpre = re.match(r"repo_name:(.*)", cv)
                ure = re.match(r"user:(.*)", cv)
                # Token to take secret
                # pls register your own secrets in Action setting before hands with your own token
                token = ${{ secrets.MYSECTOKEN }}

                if fre:
                    pFolder = fre.group(1)
                elif rre:
                    rootDomain = rre.group(1)
                elif rpre:
                    repo_name = rpre.group(1)
                elif ure:
                    user=ure.group(1)
                else:
                    print("Failed!")
                    return [None, None, None, None, None]

    print("Config Set Loaded!")
    return [token, pFolder, rootDomain, repo_name, user]

#=======================================================
# Generate one issue for comment
#   - output: True/False
#=======================================================

def batchInit(fList):
    global token, pFolder, rootDomain, repo_name, user
    session = requests.Session()
    session.auth = (user, token)
    session.headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Retry-After': '30',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.59 Safari/537.36 Edg/85.0.564.30'
    }
    # Not initialization part listed
    # But maybe it's not so necessary to run that! Just to try to create one by one
    # So , to obsolete below codes (otherwise it need even furhter handling to paging result (max 100 in one round, urgly, not necesary!)
    # existing_comments = get_comments(session=session)
    # not_initialized = list(set(fList) ^ set(existing_comments))
    not_initialized = list(set(fList))
    init_gitalk(session=session,not_initialized=not_initialized) 
    return True

#=======================================================
# Get comments based on condition 
#   - output: issues (comments threads)
#       with : "<url> <label> <title>" as unique label
#=======================================================

def get_comments(session, md5_label=''):
    global token, pFolder, rootDomain, repo_name, user
    issues = []
    url = 'https://api.github.com/repos/' + user + '/' + repo_name + '/issues?q=is&labels=Gitalk,' + md5_label
    r = session.get(url=url)
    data = json.loads(r.text)
    for issue in data:
        # To combine key info with "url label title"
        rurl = issue['body'].split(' ')[0]
        rlabel = issue['labels'][1]['name']
        rtitle = issue['title'].strip()
        res = "%s %s '%s'"%(rurl, rlabel, rtitle)
        issues.append(res)
    return issues
#=======================================================
# Get comments based on condition 
#   - output: issues (comments threads)
#       with : "<url> <label> <title>" as unique label
#=======================================================
def init_gitalk(session, not_initialized):
    global token, pFolder, rootDomain, repo_name, user
    github_url = "https://api.github.com/repos/" + user + "/" + repo_name + "/issues"
    for url in not_initialized:
        # 2 sec to avoid secondary limitation
        time.sleep(2)
        pres = re.match(r"(\S*) (\S*) (.*)", url) 
        # Got info from link
        link = pres.group(1)
        label = pres.group(2)
        title = pres.group(3)
        # to simplify the logic, in my case, only taking the label for the post (i.e. the slug or short link) for the gtalk_id
        gtalk_id = label
        issue = {
            'title': title,
            'body': "%s \n\n %s"%(link, title),
            'labels': ['Gitalk', label]
        }
        print('[{}] checking...'.format(title))
        is_existed = get_comments(session=session, md5_label=gtalk_id)
        if is_existed:
            print("issues [", title ,"] already exist")
            continue
        print('[{}] initializing...'.format(title))
        resp = session.post(url=github_url, data=json.dumps(issue))
        if resp.status_code == 201:
            print('Created')
        else:
            print('issuse: ', issue)
            print('failed: ', resp.text)
            try:
                date_time = datetime.datetime.fromtimestamp(int(resp.headers['x-ratelimit-reset']))
                print("===============================================================")
                print("Seems Exceeded Limitation , Period till: ", date_time)
                print("===============================================================")
            except:
                pass

            break

#=======================================================
# Scan all files
#=======================================================
def scanAllPosts():
    global token, pFolder, rootDomain, repo_name, user
    # fList
    fList = []
    print('===== Start to Prepare the Gitalk Comment =====')
    [token, pFolder, rootDomain, repo_name, user] = fetchConfig("config.ini")
    # Get the needed list
    # TODO: fList will be differnt if it's triggered by the push in github action!
    checkPostFolder(fList, pFolder)        
    # Run the gtalk trigger
    batchInit(fList)
    return
#=======================================================
# Create specified post comment
#=======================================================
def specifiedPost(filePath):
    global token, pFolder, rootDomain, repo_name, user
    # fList
    fList = []
    print('===== Start to Prepare the Gitalk Comment =====')
    [token, pFolder, rootDomain, repo_name, user] = fetchConfig("config.ini")
    # Get the needed list
    # Pick newer files
    res = parseFile(pFolder+'/'+filePath)
    if res[0]:
        fList.append("%s /%s %s"%(res[3],res[1][:48], res[2].strip()))
    # Run the gtalk trigger
    batchInit(fList)
    return

#=======
# Hello
#=======
def helloWorld(cheer=""):
    print("Hello World! " + cheer)

if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])
