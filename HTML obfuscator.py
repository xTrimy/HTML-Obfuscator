import glob, os, re, random
htmlfiles = []
cssfiles = []
jsfiles = []
n = []
fil = []
files = ''
randomn = []
f = open("htmlfiles.txt", "w")
for file in glob.glob("*.html"):
    htmlfiles.append(file)
for file in glob.glob("*.php"):
    htmlfiles.append(file)
print(htmlfiles)
for x in htmlfiles:
    fi = open(x, "r")
    fii = fi.read()
    fi.close()
    fii = re.sub(r"<!--(.|\s|\n)*?-->", "", fii)
    ffi = open(x, "w")
    ffi.write(fii.replace('\n', '').replace('  ','').replace('="', '=*').replace('"', '"\n').replace('=*', '="'))
    ffi.close()
    with open(x) as fp:
        line = fp.readline()
        while line:
            fil.append(line.strip())
            line = fp.readline()
    for y in fil:
         result = re.search('class="(.*)"', y)
         try:
            if 'fas' not in result.group(1):
                n.append(result.group(1))
                print(result.group(1))
         except:
            pass
    ffi = open(x, "w")
    ffi.write(fii.replace('\n', '').replace('   ',''))
    ffi.close()


print(n)
n = ' '.join(n).split()
n = list(set(n))
print(n)
open('new.txt', 'w').write('\n'.join(n))
rLs = ['a','b','c','d','e','f','g','h','x','y','z']
rNs = ['1','2','3','4','5','6','7','8','9','0']
rSl = ['-','--']
for file in glob.glob("stylesheets/*.css"):
    cssfiles.append(file)
print(cssfiles)
xx = 20
nf = open('newstyles.txt', "w")
nf.close()
while xx >= 1:
    for i in range(len(n)):
        if xx <= len(n[i]):
            randomName = 'x' + 'T' + '-' + random.choice(rLs) + random.choice(rLs) + random.choice(rLs) + random.choice(rSl) + random.choice(rNs) + random.choice(rNs)+ random.choice(rNs) + random.choice(rNs)+ random.choice(rNs) + random.choice(rNs)+ random.choice(rNs) + random.choice(rNs)
            print (i, n[i], '>', randomName)
            nf = open('newstyles.txt', "a")
            nf.write(n[i] + ' > ' + randomName + '\n')
            nf.close()
            randomn.append(randomName)
            for x in htmlfiles:
                fi = open(x, "r")
                fii = fi.read()
                fi.close()
                ffi = open(x, "w")
                ffi.write(fii.replace('class="' + n[i] + '"', 'class="' + randomName + '"').replace('"' + n[i] + " ", '"' + randomName + " ").replace(" " + n[i] + '"'," " + randomName + '"'))
                ffi.close()
            for x in cssfiles:
                fi = open(x, "r")
                fii = fi.read()
                fi.close()
                ffi = open(x, "w")
                ffi.write(fii.replace('.' + n[i], '.' + randomName))
                ffi.close()
            n[i] = ''
    xx -= 1

