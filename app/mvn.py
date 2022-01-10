import requests
import json
import time

from packageurl import PackageURL


def clean_path(s: str):
    return s.replace('.', '/')


def retrieve_name(group_id: str, artifact_id: str, version: str):
    return artifact_id + "-" + version + ".jar"


def retrieve_sha1(group_id: str, artifact_id: str, version: str):
    file_path = clean_path(group_id) + "/" + clean_path(
        artifact_id) + "/" + version + "/" + artifact_id + "-" + version + ".jar.sha1"
    url = f"https://repo1.maven.org/maven2/{file_path}"
    try:
        print(url)
        time.sleep(0.5)
        response = requests.get(url)
        return response.text.split(" ")[0]
    except Exception as e:
        print(e)
    return None


def get_purl(group_id: str, artifact_id: str):
    repo = 'https://search.maven.org/solrsearch'
    url = f'{repo}/select?core=gav&rows=200&wt=json&q=g:"{group_id}"+AND+a:"{artifact_id}"'
    output = []
    try:
        response = requests.get(url)
        all_docs = json.loads(response.text)['response']['docs']
        for d in all_docs:
            # form sha1 and md5 url
            sha1 = retrieve_sha1(d['g'], d['a'], d['v'])
            name = retrieve_name(d['g'], d['a'], d['v'])
            if sha1:
                ql = {'sha1': sha1, 'name': name}
                purl = PackageURL(type='maven', namespace=d['g'], name=d['a'], version=d['v'], qualifiers=ql)
                output.append(purl.to_string())

    except Exception as e:
        print(e)
    return output
