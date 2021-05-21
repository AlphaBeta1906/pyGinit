

questions = [
    {
		'type' : "input",
		"name" : "repo_name",
		"message":"Enter the name for your repo : "
	},
	{
		'type': "input",
		"name" : "description",
		"message" :"Enter description of your repo (leave blank if you dont have one) : "
	},
    {
    	'type' : "list",
    	"name" : "repo_type",
    	"message":"select your github repo type",
    	'choices': ["public","private"]
    },
    {
    	'type' : "input",
    	"name" : "token",
    	"message" : "Enter your github token, if you dont have visit : https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token"
    }
]