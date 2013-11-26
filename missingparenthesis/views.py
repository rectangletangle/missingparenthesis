

import random

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from django.core import paginator

from missingparenthesis.models import Article

def main (request) :
    articles = Article.objects.order_by('-date')[:settings.BLOG.SUMMARY_COUNT]
    return render(request, 'main.html', {'articles' : articles})

def _random_articles (articles, amount) :
    ''' Randomly suggests other articles to the user. '''
    # This should be more efficient with most RDMSs than the equivalent of <articles.order_by('?')[:amount]>

    try :
        randomly_sampled_indexes = random.sample(range(0, articles.count()-1), amount)
    except ValueError :
        # The population was smaller than the amount we wanted to sample, so we take what we can.
        return articles.all()
    else :
        return [articles.all()[index] for index in randomly_sampled_indexes]

def _suggested_articles (current_article) :

    other_articles = Article.objects.exclude(id=current_article.id)

    return _random_articles(other_articles, settings.BLOG.SUGGESTED_ARTICLES_COUNT)

def article (request, article_id) :
    try :
        article = Article.objects.get(id=article_id)
    except ObjectDoesNotExist :
        raise Http404
    else :
        return render(request, 'article.html', {'article'            : article,
                                                'suggested_articles' : _suggested_articles(article)})

def about (request) :
    return render(request, 'about.html')

def links (request) :
    return render(request, 'links.html')

def archive (request) :
    articles = Article.objects.order_by('-date')

    article_paginator = paginator.Paginator(articles, settings.BLOG.ARCHIVE_LINK_COUNT)

    try:
        article_pages = article_paginator.page(request.GET.get('page'))
    except paginator.PageNotAnInteger :
        article_pages = article_paginator.page(1)
    except paginator.EmptyPage :
        article_pages = article_paginator.page(article_paginator.num_pages)

    return render(request, 'archive.html', {'articles' : article_pages})

def faq (request) :
    return render(request, 'faq.html')

def contact (request) :
    return render(request, 'contact.html')

def robots (request) :
    return HttpResponse('User-agent: *\nDisallow:', mimetype='text/plain')

def error_403 (request) :
    return render(request, '403.html')

def error_404 (request) :
    return render(request, '404.html')

def error_500 (request) :
    return render(request, '500.html')

