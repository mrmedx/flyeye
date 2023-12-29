#@version
VERSION="flyeye 1.0"
DESCRIPTION="web forensics framework."
#@VERSION_COMMANDS
VERSION_COMMANDS=["version", "-v", "--v"]
#@wf parameters:
WHO="who"
SAID="said"
FACEBOOK="facebook"
INSTAGRAM="instagram"
FLY="fly"
FROM="from"
TO="to"
ON="on"
IN="in"
BEFORE="before"
AFTER="after"
AND="and"
OR="or"
NOT="not"
ANY="any"
COUNTRY="country"
SITE="site"
EXACT="exact"
LEAKED="leaked"
EMAIL="email"
PHONE_NUMBER="phone"
ACCESS_TOKEN="access_token"
SAVE_TO="saveto"
LOAD="load"
KEYWORDS=[LOAD,SAVE_TO,ACCESS_TOKEN,PHONE_NUMBER,EMAIL,LEAKED,EXACT, SITE,COUNTRY,ANY,NOT, OR, AND, AFTER,BEFORE,IN,ON,TO,FROM,FLY, SAID,WHO]
#@error msg
INVALD_COUNTRY_CODE="Invalid Coutry code: "
COUNTRY_CODE_EXAMPLE=", Coutry code example:us,US"
CONTINUE_WITH_NO_COUNTRY="Proceeding with no specified target country..."
INVALID_URL="Invalid url: "
INVALID_LEAK_TYPE="Invalid leak type: "
INVALID_LEAK_TYPE_MSG=", available types:email, phone, access_token."
INVALID_DATE="Invalid Date: "
VALID_DATE_EXAMPLE=", date formate:Y-M-D, 2023-01-01"

#@HELP_COMMANDS
HELP_COMMANDS=["help", "-h", "--h"]
#@HELP_MENU
HELP_MENU={
       WHO: {
                'description': 'info about an event.',
                'example': 'python flyeye.py who fly from example.com to des.com'
        },
        SAID: {
                'description': 'find words mentioned in a source',
                'example': 'python flyeye.py who said "download now" on example.com'
        },

        FLY: {
                'description': 'info about web traffic.',
                'example': 'python flyeye.py who fly from example.com to des.com in us'
        },
        FROM: {
                'description': 'the source website.',
                'example': 'python flyeye.py who fly from example.com to des.com'
        },

        TO: {
                'description': 'the destination website.',
                'example': 'python flyeye.py who fly from example.com to des.com'
        },
        ON: {
                'description': 'the target website.',
                'example': 'python flyeye.py who said "hello world" on example.com'
        },
        IN: {
                'description': 'the target country.',
                'example': 'python flyeye.py who said "hello world" in us'
        },
        BEFORE: {
                'description': 'search before the given date <Y-M-D>',
                'example': 'python flyeye.py who said "hello world" before 2023-01-01'
        },

        AFTER: {
                'description': 'search after the given date <Y-M-D>',
                'example': 'python flyeye.py who said "hello world" after 2023-01-01'
        },
        LEAKED: {
                'description': 'find leaked data <email, access_token, phone>',
                'example': 'python flyeye.py who leaked email on example.com'
        },
        EMAIL: {
                'description': 'the leaked data type',
                'example': 'python flyeye.py who leaked email on example.com'
        },
        PHONE_NUMBER: {
                'description': 'the leaked data type',
                'example': 'python flyeye.py who leaked phone on example.com'
        },
        ACCESS_TOKEN: {
                'description': 'the leaked data type',
                'example': 'python flyeye.py who leaked access_token on example.com'
        },
         ANY: {
                'description': 'used before the site keyword to search for any site',
                'example': 'python flyeye.py who fly from any site to example.com'
        },
        SITE: {
                'description': 'used after the any keyword to search for any site',
                'example': 'python flyeye.py who fly from example.com to any site'
        },
         EXACT: {
                'description': 'search for exact word',
                'example': 'python flyeye.py who said exact "hello world" on example.com'
        },
        AND: {
                'description': 'logical and',
                'example': 'python flyeye.py who said exact "hello world" and said "hi" on example.com'
        },
         OR: {
                'description': 'logical or',
                'example': 'python flyeye.py who said exact "hello world" or said "hi" on example.com'
        },
         NOT: {
                'description': 'logical not',
                'example': 'python flyeye.py who said exact "hello world" and not said "hi" on example.com'
        },
         SAVE_TO: {
                'description': 'save the results to a local file',
                'example': 'python flyeye.py saveto results.json who said exact "hello world" on example.com'
        },
        LOAD: {
                'description': 'load a flyeye saved results and perform a task',
                'example': 'python flyeye.py load results.json who said exact "download this file"'
        },
        str(HELP_COMMANDS): {
                'description': 'show this help menu.',
                'example': 'python flyeye.py help"'
        },
}
#@HELP_MENU end.