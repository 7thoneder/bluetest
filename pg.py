import os

#Here is where I would imput the new repo name & the private repo url
reponame = input('Repo Name? ')
repourl = input('Repo URL? ')

#Here the URL's are defined
sthonederurl = repourl + reponame
#This is the hardcoded private repo url
sthonederurlp = 'https://github.com/7thoneder/'

#These commands will only fire off if the below IF statement is true
cmd = 'git remote add origin ' + sthonederurl
cmd2 = 'git push origin master'

#This checks that the URL I typed in matches the hardcoded private repo url
if sthonederurlp == repourl:
    os.system(cmd)
    os.system(cmd2)
else:
    print('Wrong URL!')