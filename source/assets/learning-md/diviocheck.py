from urllib import request, error
from json import loads
from re import search, RegexFlag

print("Checking repos for divio docs structure...")
try: 
    with open('.cache', 'r') as file:
        prevUsername = file.read()
except:
    prevUsername = ''

username = input(f"GitHub username [{prevUsername}]: ") or prevUsername
with open('.cache', 'w') as file:
    file.write(username)

OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

TUTORIALS = r"^#.*tutorial"
HOW_TO = r"^#.*how\W*to"
REFERENCE = r"^#.*reference"
EXPLANATION = r"^#.*(explanation|discussion|background\W*material)"

# Centerring after the function seems to not work
def ok(center, string="OK"):
    return f"{OKGREEN}{string.center(center)}{ENDC}"

def nok(center, string="NOK"):
    return f"{FAIL}{string.center(center)}{ENDC}"

def getReadmeContents(username, reponame, branch):
    url = f"https://raw.githubusercontent.com/{username}/{reponame}/{branch}/README.md"
    try:
        with request.urlopen(url) as req:
            data = req.read().decode(req.headers.get_content_charset())  # https://stackoverflow.com/a/19156107
    except error.HTTPError as err:
        if err.code == 404:
            return ''
        else: 
            raise err
    return data

def regexIn(needle, haystack):
    return bool(search(needle, haystack, RegexFlag.IGNORECASE | RegexFlag.MULTILINE))



headers = ["     repository     ", "tutorials", "how to's", "explanation(s)", "reference(s)"]
def headerUnderline(i):
    headers[i]

# Table generation
print("|", end="")
for header in headers:
    print(f" {header} ", end="|")
print("\n|", end="")
for header in headers:
    print(f" {'-' * len(header)} ", end="|")
print()


with request.urlopen(f"https://api.github.com/users/{username}/repos") as req:
    repos = loads(req.read())
    for repo in repos:
        reponame = repo['name']
        main = repo['default_branch']

        content = getReadmeContents(username, reponame, main)

        repoHeaderLength = len(headers[0])
        reponamePadded = reponame[:repoHeaderLength].center(repoHeaderLength)

        print(f"| {reponamePadded} ", end="|")

        for i, regex in enumerate([TUTORIALS, HOW_TO, REFERENCE, EXPLANATION]):
            length = len(headers[i+1])  # The first header is already handled

            result = ok(length) if regexIn(regex, content) else nok(length)


            print(f" {result} ", end="|")
        print()

        



