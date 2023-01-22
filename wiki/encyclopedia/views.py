from django.shortcuts import render
import markdown2
from . import util
import random

app_name = 'entry'
AllEntries = []


def md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown2.Markdown()
    if content == None:
        return None

    else:
        return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    hcontent = md_to_html(title)

    if hcontent == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page Not Found"
        })

    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": hcontent
        })


def search(request):
    if request.method == "POST":
        search = request.POST['q']
        hcontent = md_to_html(search)

        if hcontent is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": search,
                "content": hcontent
            })
        else:
            lists = []
            allEntries = util.list_entries()
            for ent in allEntries:
                if search.lower() in ent.lower():
                    lists.append(ent)

            return render(request, "encyclopedia/search.html", {
                "lists": lists
            })


def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")

    else:
        title = request.POST['title']
        content = request.POST['mcontent']

        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Page Already Exist"
            })

        else:
            util.save_entry(title, content)
            hcontent = md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": hcontent
            })


def edit(request):
    if request.method == "POST":

        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })


def save(request):
    if request.method == "POST":
        title = request.POST['edit_title']
        content = request.POST['edit_mcontent']
        util.save_entry(title, content)
        hcontent = md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": hcontent
        })


def randomPage(request):
    AllEntries = util.list_entries()
    randomEntry = random.choice(AllEntries)
    hcontent = md_to_html(randomEntry)
    return render(request, "encyclopedia/entry.html", {
        "title": randomEntry,
        "content": hcontent
    })


def delete(request):
    title = request.POST['delete_title']
    content = util.get_entry(title)
    util.delete_entry(title, content)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
