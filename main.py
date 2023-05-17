from urllib.parse import urlparse, parse_qs


def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    parameters = parsed_url.query
    result = dict((key, value[0] if isinstance(value, list) else value)
                  for key, value in parse_qs(parameters).items())
    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/?time=2312&wanttosleep=true&hungry=yes') == {'time': '2312',
                                                                                   'wanttosleep': 'true',
                                                                                   'hungry': 'yes'}
    assert parse('https://example.com/!') == {}
    assert parse('https://example.com/12345rbb') == {}
    assert parse('https://ithillel.ua/?lessons=32&shouldhave=64') == {'lessons': '32', 'shouldhave': '64'}
    assert parse('https://ithillel.ua/?height=171&weight=79&fat=yes') == {'height': '171',
                                                                          'weight': '79',
                                                                          'fat': 'yes'}
    assert parse('https://ithillel.ua/?iq=70&dumb=true') == {'iq': '70', 'dumb': 'true'}
    assert parse('http://google.com/?putin=huilo&lalalala=lalalala') == {'putin': 'huilo', 'lalalala': 'lalalala'}
    assert parse('http://google.com/?example10=almost') == {'example10': 'almost'}
    assert parse('http://google.com/?funhomework=false') == {'funhomework': 'false'}
    assert parse('http://google.com/?fucking=really&forgot=howToCount') == {'fucking': 'really', 'forgot': 'howToCount'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
