[출처](https://im-developer.tistory.com/166)

[**[HTTP\] HTTP Method 정리 / GET vs POST 차이점**](https://im-developer.tistory.com/166)

[Computer Science](https://im-developer.tistory.com/category/Computer Science) 2019. 9. 10. 22:06



![img](https://blog.kakaocdn.net/dn/kHOj6/btqydQELTLd/F8eugrrqVzNEaebLkn1AhK/img.jpg)이미지 출처: https://dev.to/williamragstad/how-to-use-ajax-3b5e



 

 

 

GET이나 POST는 매우 자주 쓰는 HTTP 메소드들이다.

아마 제일 많이 쓰지 않나 싶다. 

 

근데 정확히 두 개가 어떻게 다른지,

어떤 특징을 가지고 있는지 잘 모르겠어서 정리해보려고 한다.

아래 글들은 영문 블로그 내용을 번역한 것이고 

원문 글에 대한 출처는 글 하단에 있다.

 

 

 

------

 

### **GET**

GET 메소드는 주로 데이터를 **읽거나(\**Read)\**** **검색(\**Retrieve\**)**할 때에 사용되는 메소드이다. 만약에 GET요청이 성공적으로 이루어진다면 XML이나 JSON과 함께 200 (Ok) HTTP 응답 코드를 리턴한다. 에러가 발생하면 주로 404 (Not found) 에러나 400 (Bad request) 에러가 발생한다.

 

HTTP 명세에 의하면 GET 요청은 오로지 데이터를 읽을 때만 사용되고 수정할 때는 사용하지 않는다. 따라서 이런 이유로 사용하면 안전하다고 간주된다. 즉, 데이터의 변형의 위험없이 사용할 수 있다는 뜻이다. 게다가 GET 요청은 **idempotent**하다. 즉, 같은 요청을 여러 번 하더라도 변함없이 항상 같은 응답을 받을 수 있다. 그러므로 GET을 데이터를 변경하는 등의 안전하지 않은 연산에 사용하면 안된다.

 

 

 

### **POST**

POST 메소드는 주로 새로운 리소스를 **생성(create)**할 때 사용된다. 조금 더 구체적으로 POST는 하위 리소스(부모 리소스의 하위 리소스)들을 생성하는데 사용된다. 성공적으로 creation을 완료하면 201 (Created) HTTP 응답을 반환한다. POST 요청은 안전하지도 않고 idempotent하지도 않다. 다시 말해서 같은 POST 요청을 반복해서 했을 때 항상 같은 결과물이 나오는 것을 보장하지 않는다는 것이다. 그러므로 두 개의 같은 POST 요청을 보내면 같은 정보를 담은 두 개의 다른 resource를 반환할 가능성이 높다.

 

 

 

### **GET vs POST**

HTTP POST 요청은 클라이언트에서 서버로 전송할 때 추가적인 데이터를 body에 포함할 수 있다. 반면에 GET 요청은 모든 필요한 데이터를 URL에 포함하여 요청한다. HTML의 **<form>**태그에 **method="POST"** 또는 **method="GET"**(기본값)을 모두 사용할 수 있다. 만약에 GET 메소드를 사용하면 모든 form data는 URL로 인코딩되어 action URL에 query string parameters로 전달된다. POST 메소드를 사용하면 form data는 HTTP request의 message body에 나타날 것이다.

 

 

 

|                                      | **GET**                                                      | **POST**                                                     |
| ------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **History**                          | Parameters remain in browser history because they are part of the URL.파라미터들은 URL의 일부분이기 때문에 브라우저 히스토리에 남는다. | Parameters are not saved in browser history.파라미터들이 브라우저 히스토리에 저장되지 않는다. |
| **Bookmarked**                       | Can be bookmarked.요청 파라미터들이 URL로 인코딩되므로 즐겨찾기가 가능하다. | Can not be bookmarked.요청 파라미터들이 request body에 포함되고 request URL에 나타나지 않으므로 즐겨찾기가 불가능하다. |
| **button/re-submit behaviour**       | GET requests are re-executed but may not be re-submitted to server if the HTML is stored in the browser cache.GET 요청이 다시 실행되더라도 브라우저 캐시에 HTML이 저장되어있다면 서버에 다시 submit되지 않는다. | The browser usually alerts the user that data will need to be re-submitted.브라우저가 보통 사용자에게 데이터가 다시 submit되어야 한다고 alert을 준다. |
| **Encoding type(enctype attribute)** | application/x-www-form-urlencoded                            | multipart/form-data or application/x-www-form-urlencoded Use multipart encoding for binary data. |
| **Parameters**                       | can send but the parameter data is limited to what we can stuff into the request line (URL). Safest to use less than 2K of parameters, some servers handle up to 64K전송 가능하지만 URL에 넣을 수 있는 파라미터 데이터가 제한된다. 2K이하로 사용하는 것이 안전하며 몇몇 서버들은 64K까지 다룬다. | Can send parameters, including uploading files, to the server.서버에 파일 업로드하는 것을 포함하여 파라미터를 전송할 수 있다. |
| **Hacked**                           | Easier to hack for [script kiddies](https://en.wikipedia.org/wiki/Script_kiddie)script kiddies에 의해 해킹되기 쉽다. | More difficult to hackGET에 비해 좀 더 해킹하기 어렵다.      |
| **Restrictions on form data type**   | Yes, only ASCII characters allowed.오직 ASCII characters만 허용된다. | No restrictions. Binary data is also allowed.제한이 없다. binary data도 허용된다. |
| **Security**                         | GET is less secure compared to POST because data sent is part of the URL. So it's saved in browser history and server logs in plaintext.GET은 POST에 비해 보안에 약하다. 그 이유는 데이터가 URL의 일부로 전송되고 그 때문에 브라우저 히스토리에 저장되며 서버가 플레인 텍스트로 로그를 남기기 때문이다. | POST is a little safer than GET because the parameters are not stored in browser history or in web server logs.POST는 GET에 비해 보안에 조금 더 안전하다. 그 이유는 파라미터들이 브라우저 히스토리나 서버 로그에 저장되지 않기 때문이다. |
| **Restrictions on form data length** | Yes, since form data is in the URL and URL length is restricted. A safe URL length limit is often 2048 characters but varies by browser and web server.form data가 URL에 포함되고 URL 길이가 제한되기 때문에 form data의 길이도 제한된다. 안전한 URL 길이는 2048 characters이나 브라우저나 웹 서버에 따라 달라진다. | No restrictions제한이 없다.                                  |
| **Usability**                        | GET method should not be used when sending passwords or other sensitive information.GET 메소드는 비밀번호와 같은 민감한 정보들을 전송하는데 사용해선 안된다. | POST method used when sending passwords or other sensitive information.POST 메소드는 비밀번호와 같은 민감한 정보를 전송하는데 사용된다. |
| **Visibility**                       | GET method is visible to everyone (it will be displayed in the browser's address bar) and has limits on the amount of information to send.GET 메소드는 모두에게 보여진다. (브라우저의 주소창에 그대로 보여지고 그에 따라 전송가능한 정보의 양도 제한된다.) | POST method variables are not displayed in the URL.POST 메소드는 URL에 보여지지 않는다. |
| **Cached**                           | Can be cachedGET은 idempotent하기 때문에 캐시가 된다.(같은 요청을 여러 번 보내도 항상 같은 응답이 온다.) | Not cachedPOST는 idempotent하지 않기 때문에 캐시가 되지 않는다.(같은 요청을 여러 번 보내도 다른 응답이 올 수 있다.) |

 

 

 



[출처](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests)

HTTP **POST** requests supply additional data /from the client (browser) to the server in the message body. 

HTTP POST요청은 데이터를 제공합니다./ 클라이언트(브라우저)로 부터 서버에게 / 메세지 본문로

In contrast, **GET** requests include all required data in the URL. 

그에 반해서/ GET요청은 모든 요구된 데이터를 포함한다. / URL안에

Forms in HTML can use either method by specifying **method="POST"** or **method="GET"** (default) in the **<form>** element. 

HTML의 Forms는 다른 메소드를 이용 할 수 있다./ method="POST" or method="GET"을 명시함으로써/ 요소 안에

The method specified determines how form data is submitted to the server. 

그 지정된 방법에 따라 결정됩니다./ 폼의 데이터가 보내지는지 방법이/ 서버에

When the method is GET, all form data is encoded into the URL, appended to the **action** URL as query string parameters. With POST, form data appears within the message body of the HTTP request.

GET메소드를 사용 할 때, 모든 form의 데이터는 URL로 변환된다. / 작업URL이 문자열 파라미터 쿼리로 추가된다. / POST는 form데이터를 본문 메시지 안에 나타낸다./HTTP의 요청의

## Comparison chart

| [![Edit this comparison chart](https://static.diffen.com/css/img/edit.png)](https://www.diffen.com/difference/Special:EditTable?diffenVal1=GET+(HTTP)&diffenVal2=POST+(HTTP)) | GET                                                          | POST                                                         |
| -----------------------------------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------- |
|                                                              | current rating is 4.12/5[1](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests#j=1&q=350)[2](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests#j=2&q=350)[3](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests#j=3&q=350)[4](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests#j=4&q=350)[5](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests#j=5&q=350)**(1238 ratings)** | current rating is 4.43/5[1](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests#j=1&q=351)[2](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests#j=2&q=351)[3](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests#j=3&q=351)[4](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests#j=4&q=351)[5](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests#j=5&q=351)**(1357 ratings)** |
|                                                      History | Parameters remain in browser history because they are part of the URL | Parameters are not saved in browser history.                 |
|                                                   Bookmarked | Can be bookmarked.                                           | Can not be bookmarked.                                       |
|                              BACK button/re-submit behaviour | GET requests are re-executed but may not be re-submitted to server if the HTML is stored in the browser cache. | The browser usually alerts the user that [data](https://www.diffen.com/difference/Data_vs_Information) will need to be re-submitted. |
|                            Encoding type (enctype attribute) | application/x-www-form-urlencoded                            | multipart/form-data or application/x-www-form-urlencoded Use multipart encoding for binary data. |
|                                                   Parameters | can send but the parameter data is limited to what we can stuff into the request line (URL). Safest to use less than 2K of parameters, some servers handle up to 64K | Can send parameters, including uploading files, to the server. |
|                                                       Hacked | Easier to hack for script kiddies                            | More difficult to hack                                       |
|                               Restrictions on form data type | Yes, only ASCII characters allowed.                          | No restrictions. Binary data is also allowed.                |
|                                                     Security | GET is less secure compared to POST because data sent is part of the URL. So it's saved in browser history and server logs in plaintext. | POST is a little safer than GET because the parameters are not stored in browser history or in [web server](https://www.diffen.com/difference/Application_Server_vs_Web_Server) logs. |
|                             Restrictions on form data length | Yes, since form data is in the URL and URL length is restricted. A safe URL length limit is often 2048 characters but varies by browser and web server. | No restrictions                                              |
|                                                    Usability | GET method should not be used when sending passwords or other sensitive information. | POST method used when sending passwords or other sensitive information. |
|                                                   Visibility | GET method is visible to everyone (it will be displayed in the browser's address bar) and has limits on the amount of information to send. | POST method variables are not displayed in the URL.          |
|                                                       Cached | Can be cached                                                | Not cached                                                   |

## Differences in Form Submission

The fundamental difference between *METHOD="GET"* and *METHOD="POST"* is that they correspond to **different HTTP requests**, as defined in the [HTTP](http://www.w3.org/Protocols/) [specifications](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9). The submission process for both methods begins in the same way - a [form data set](http://www.w3.org/TR/REC-html40/interact/forms.html#form-data-set) is constructed by the browser and then encoded in a manner specified by the *enctype* attribute. For *METHOD="POST* the *enctype* attribute can be *multipart/form-data* or *application/x-www-form-urlencoded*, whereas for *METHOD="GET"*, only *application/x-www-form-urlencoded* is allowed. This form data set is then transmitted to the server.

For form submission with METHOD="GET", the browser constructs a URL by taking the value of the *action* attribute, appending a *?* to it, then appending the form data set (encoded using the application/x-www-form-urlencoded content type). The browser then processes this URL as if following a link (or as if the user had typed the URL directly). The browser divides the URL into parts and recognizes a host, then sends to that host a GET request with the rest of the URL as argument. The server takes it from there. Note that this process means that the form data are restricted to ASCII codes. Special care should be taken to encode and decode other types of characters when passing them through the URL in ASCII format.

Submission of a form with METHOD="POST" causes a POST request to be sent, using the value of the *action* attribute and a message created according to the content type specified by the *enctype* attribute.



### Pros and Cons

Since form data is sent as part of the URL when *GET* is used --

- Form data are restricted to ASCII codes. Special care should be taken to encode and decode other types of characters when passing them through the URL in ASCII format. On the other hand, binary data, images and other files can all be submitted through *METHOD="POST"*
- All form data filled in is visible in the URL. Moreover, it is also stored in the user's web browsing history/logs for the browser. These issues make *GET* less secure.
- However, one advantage of form data being sent as part of the URL is that one can bookmark the URLs and directly use them and completely bypass the form-filling process.
- There is a limitation on how much form data can be sent because [URL lengths are limited](http://stackoverflow.com/questions/2659952/maximum-length-of-http-get-request).
- Script kiddies can more easily expose vulnerabilities in the system to hack it. For example, Citibank was hacked by changing account numbers in the URL string.[[1\]](http://channel9.msdn.com/Forums/Coffeehouse/Citibank-hacked-By-changing-account-numbers-In-the-URL) Of course, experienced hackers or web developers can expose such vulnerabilities even if POST is used; it's just a little bit harder. In general, the server must be suspicious of any data sent by the client and guard against [Insecure Direct Object References](https://www.owasp.org/index.php/Top_10_2010-A4-Insecure_Direct_Object_References).

## Differences in Server-Side Processing

In principle, processing of a submitted form data depends on whether it is sent with *METHOD="GET"* or *METHOD="POST"*. Since the data is encoded in different ways, different decoding mechanisms are needed. Thus, generally speaking, changing the METHOD may necessitate a change in the script which processes the submission. For example, when [using the CGI interface](http://hoohoo.ncsa.uiuc.edu/cgi/forms.html), the script receives the data in an environment variable (QUERYSTRING) when *GET* is used. But when *POST* is used, form data is passed in the standard input stream (*stdin*) and the number of bytes to be read is given by the Content-length header.

## What happens when GET and POST variables conflict?

In some languages such as PHP, the information from GET and POST parameters, in addition to being available separately, is also combined into a convenience variable e.g., *$_REQUEST* in PHP. If there is a conflict—i.e., the same parameter name is used with different values in GET and POST—then the conflict is resolved with certain rules. In the case of PHP, precedence is decided by the [*variables_order*](http://php.net/manual/en/ini.core.php#ini.variables-order) configuration directive. The default order is EGPCS (environment, GET, POST, Cookie, Server). This means the variable in $_GET gets precedence over $_POST, which in turn gets precedence over $_COOKIE.

<iframe id="google_ads_iframe_/18190176,3630741/AdThrive_Content_3/6027f2ba0df047c1444d6afa_0" name="google_ads_iframe_/18190176,3630741/AdThrive_Content_3/6027f2ba0df047c1444d6afa_0" title="3rd party ad content" width="336" height="280" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" role="region" aria-label="Advertisement" tabindex="0" data-load-complete="true" data-google-container-id="b" style="box-sizing: border-box; border: 0px; vertical-align: bottom;"></iframe>

## Recommended Usage

GET is recommended when submitting "idempotent" forms - those that do not 'significantly alter the state of the world'. In other words, forms that involve database queries only. Another perspective is that several idempotent queries will have the same effect as a single query. If database updates or other actions such as triggering emails are involved, the usage of POST is recommended.

From the [Dropbox developer blog](https://blogs.dropbox.com/developers/2015/03/limitations-of-the-get-method-in-http/):

> a browser doesn’t know exactly what a particular HTML form does, but if the form is submitted via HTTP GET, the browser knows it’s safe to automatically retry the submission if there’s a network error. For forms that use HTTP POST, it may not be safe to retry so the browser asks the user for confirmation first.

A "GET" request is often cacheable, whereas a "POST" request can hardly be. For query systems this may have a considerable efficiency impact, especially if the query strings are simple, since caches might serve the most frequent queries.

In certain cases, using *POST* is recommended even for idempotent queries:

- **If the form data would contain non-ASCII characters** (such as accented characters), then *METHOD="GET"* is inapplicable in principle, although it may work in practice (mainly for [ISO Latin 1 characters](http://www.cs.tut.fi/~jkorpela/chars.html#latin1)).
- **If the form data set is large** - say, hundreds of characters - then *METHOD="GET"* may cause practical problems with implementations which cannot handle that long URLs.
- You might wish to avoid *METHOD="GET"* in order to make it less visible to users how the form works, especially in order to make "hidden" fields (INPUT TYPE="HIDDEN") more hidden by not appearing in the URL. But even if you use hidden fields with *METHOD="POST"*, they will still appear in the HTML source code.

## What about HTTPS?

*Updated May 15, 2015: Specifically when using HTTPS (HTTP over TLS/SSL), does POST offer any more security than GET?*

<iframe id="google_ads_iframe_/18190176,3630741/AdThrive_Content_4/6027f2ba0df047c1444d6afa_0" name="google_ads_iframe_/18190176,3630741/AdThrive_Content_4/6027f2ba0df047c1444d6afa_0" title="3rd party ad content" width="336" height="280" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" role="region" aria-label="Advertisement" tabindex="0" data-load-complete="true" data-google-container-id="7" style="box-sizing: border-box; border: 0px; vertical-align: bottom;"></iframe>

This is an interesting question. Say you make a GET request to a webpage:

```
 GET https://www.example.com/login.php?user=mickey&passwd=mini
```

Assuming that your Internet connection is being monitored, what information about this request will be available to the snooper? If POST is used instead, and the user and passwd data is included in POST variables, will that be more secure in the case of HTTPS connections?

The answer is no. If you make such a GET request, only the following information will be known to the attacker monitoring your web traffic:

1. The fact that you made an HTTPS connection
2. The hostname – www.example.com
3. The total length of the request
4. The length of the response

The path part of the URL — i.e., the actual page requested, as well as the query string parameters — are protected (encrypted) while they are "over the wire" i.e., in transit on their way to the destination server. The situation is exactly the same for POST requests.

The *POST* method does still retain one advantage even in the case of HTTPS, however. Web servers tend to log the entire requested URL in plain text in their access logs; so sending sensitive information over GET is not a good idea. This applies irrespective of whether HTTP or HTTPS is used.





GET and POST are two commonly used HTTP methods for sending data from a client to a server.

Differences:

1. Purpose: GET is used to retrieve data from a server, while POST is used to submit data to a server for processing.
2. Data size: GET requests have a limit on the amount of data that can be sent, whereas POST requests have no such limit.
3. Bookmarking: GET requests can be bookmarked and cached, while POST requests cannot.
4. Security: GET requests are not secure as they are visible in the URL and can be cached, while POST requests are more secure as the data is not visible in the URL and not cached.
5. Idempotency: GET requests are idempotent, meaning that repeated requests result in the same response, while POST requests are not idempotent.

Comparison: GET is suitable for simple and safe operations, such as retrieving data from a server, while POST is suitable for more complex and sensitive operations, such as submitting form data or uploading a file. The choice between GET and POST depends on the nature of the request and the data being sent.

GET 및 POST는 클라이언트에서 서버로 데이터를 전송하기 위해 일반적으로 사용되는 두 가지 HTTP 방법입니다.

차이점:

목적: GET은 서버에서 데이터를 검색하는 데 사용되고 POST는 데이터를 처리하기 위해 서버에 제출하는 데 사용됩니다.
데이터 크기: GET 요청은 전송할 수 있는 데이터 양에 제한이 있는 반면, POST 요청은 이러한 제한이 없습니다.
북마크: GET 요청은 북마크하고 캐시할 수 있지만 POST 요청은 할 수 없습니다.
보안: GET 요청은 URL에 표시되고 캐시될 수 있으므로 안전하지 않은 반면, POST 요청은 URL에 표시되지 않고 캐시되지 않으므로 더 안전합니다.
Idempotency: GET 요청은 Idempotent입니다. 즉, 반복되는 요청은 동일한 응답을 초래하는 반면 POST 요청은 Idempotent가 아닙니다.
비교:
GET은 서버에서 데이터를 검색하는 것과 같은 간단하고 안전한 작업에 적합한 반면, POST는 양식 데이터 제출 또는 파일 업로드와 같은 더 복잡하고 민감한 작업에 적합합니다. GET과 POST 중에서 선택할 수 있는 것은 요청의 특성과 전송되는 데이터에 따라 달라집니다.