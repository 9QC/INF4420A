python -c "import random,string, crypt;
randomSalt = ''.join(random.sample(string.ascii_letters,8));
print 'Sel : ' + randomSalt;
print crypt.crypt('monMotDePasseSecret', '\$6\$%s\$' % randomSalt)
