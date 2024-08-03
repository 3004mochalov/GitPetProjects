import re


def main(text):
    text = text.replace(" ", "").replace("\n", "")
    keys = re.findall(r'"(.*?)"', text)
    val = re.findall(r'\((.*?)\)', text)
    res = dict()
    for i in range(len(val)):
        res[keys[i]] = val[i].replace("`", "").split('.')
    return res


print(main('do <section>loc list( `ceinbe_211 . `zatiso_946 . `teus )\n==>"veis_857". </section>, <section> loc list( `gerila . `ceen .\n`leesbe_37)==> "anxe_534".</section>, end'))
