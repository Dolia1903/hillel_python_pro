from urllib.parse import urlparse, parse_qs
from http.cookies import SimpleCookie


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


def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)

    cookies = {k: v.value for k, v in cookie.items()}
    return cookies


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Vova;age=30') == {'name': 'Vova', 'age': '30'}
    assert parse_cookie('sphere=IT;profession=ServiceOps') == {'sphere': 'IT', 'profession': 'ServiceOps'}
    assert parse_cookie('country=Ukraine; lng = UA; timezone = GMT+3') == {'country': 'Ukraine', 'lng': 'UA',
                                                                           'timezone': 'GMT+3'}
    assert parse_cookie('moskali=yes; dead = true; skiko = 200000') == {'moskali': 'yes', 'dead': 'true',
                                                                        'skiko': '200000'}
    assert parse_cookie('tired=true;example = 5') == {'tired': 'true', 'example': '5'}
    assert parse_cookie('When will this shit end?') == {}
    assert parse_cookie('NotNow=no;okay=true') == {'NotNow': 'no', 'okay': 'true'}
    assert parse_cookie('CanIPleaseJustDie=False') == {'CanIPleaseJustDie': 'False'}
    assert parse_cookie('done=9; left=1;') == {'done': '9', 'left': '1'}
    assert parse_cookie('Dobbie=Elf; Got=Sock; Can=Sleep') == {'Dobbie': 'Elf', 'Got': 'Sock', 'Can': 'Sleep'}
