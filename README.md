https://vrgl.ir/d2xsv


 فلسک (Flask) یکی از فریمورک های قوی و محبوب Python هست که در ایرانم بسیار محبوبه نسبتا و هر روز هم داره محبوب تر میشه و برنامه های بیشتری باهاش نوشته میشه اما در این بین همیشه بحث امنیت (web security) یه مشکل اساسی بود.

 چون فلسک یه میکروفریمورک حساب میشه عملا با خیلی از ابزار ها نمی یاد و برنامه نویس باید یا خودش اونها رو پیاده سازی کنه یا از ابزار های سوم شخصی که توسعه دادن میشه و متن باز هستن استفاده کنه که خیلی از مواقع چون برنامه نویس درست بعضی از موارد رو کانفیگ نکرده باعث بروز مشکلات جدی میشه
 برعکس خیلی از فریمورک هایی مثل لاراول (PHP.laravel) - جنگو (Python.Django) - سی شارپ (CSHARP.ASP .NET)  و ... که عملا خیلی از موارد امنیتی و غیر توی خودشون دارن و از قبل هم یه کانفیگ اولیه شدن و آماده استفاده هستن ولی توی فلسک اینجوری نیست !

  برای مثال یه برنامه ساده Hello World ساده رو توی فلسک رو میشه توی یک فایل (app.py) ساده با همین چند خط زیر نوشت :) !

 from flask import Flask
 app = Flask(__name__) 

@app.route(/,  methods=[GET]) 
def index_view_page():
     # index view return Hello World Text
      return Hello World

  if __name__ == __main__:
     app.run() # run flask application 

و بعدش برای اجرای برنامه کافیه یا برنامه رو به صورت مستقیم با Python ران کنیم یا با دستور flask run اجرا کنیم
$ python3 app.py
 or 
flask run
 
* Debug mode: off WARNING: This is a development server. Do not use it in a production 
  deployment. Use a production WSGI server instead. 
 * Running on http://127.0.0.1:5000
 Press CTRL+C to quit
زمانی که برنامه با موفقیت اجرا بشه خروجی باید چیزی مثل زیر باشه:

python3 app.py



flask run

web application
خب حالا برای اینکه برنامه ما امن باشه باید چند تا چیز رو همیشه رعایت کنیم





01.SECRET_KEY
همیشه برای برنامه اتون سعی کند یه SECRET_KEY قوی بزارید, به این دلیل که فلسک از این SECRET_KEY خیلی جاها استفاده میکنه مثال برای رمزنگاری داده ها و ....
 یه مثال ساده اش میشه SESSION ها که توی cookie سمت کاربر ذخیره میشه اما رمز (رمزنگاری) میشه که کاربر نتونه دستکاریش کنه
برای تنظیم secret_key هم میتونید به روش های مختلفی عمل کنید یه روش معمولیش اینه از طریق آبجکت اصلی app این کارو انجام بدید
app.config[SECRET_KEY] = os.urandom(24) or string Secret key
برای درست کردن رشته های تصادفی هم میتونید از کتابخونه های زیادی استفاده کنید ولی من خودم os, secrets رو یشنهاد میکنم چون build in (داخلی - دیفالت در خود Python قرار دارند) هستند 
In [1]: import os
In [2]: import secrets
In [3]: os.urandom(6)
Out[3]: b iI3C\x9c8
In [4]: secrets.token_hex(6)
Out[4]: 1c918c95737f
In [5]: 



02.DEBUG MODE
یکی از اشتباهات رایج برنامه نویس ها اینکه که فراموش می کنند DEBUG رو توی برنامه اشون FALSE کنند و برنامه رو روی حالت production قرار بدن که معمولا سبب میشه یه سری اطلاعات محرمانه گاهی افشا بشن
حتما حواستون باشه که برنامه اتون در حالت production قرار داشته باشه 
من خودم معمولا یه sccript دارم که در background اجرا میشه و چک میکنه اگر توی سرور debug = True بود خودش میاد debug رو False میکنه 




03.Don’t Store Sensitive Data in Cookies
اطلاعات حساس رو در session کاربر قرار ندید چون session ها در سمت کاربر توی cookie ذخیره میشن امن نیست اطلاعات حساس رو در session ذخیره کنید 
اگر نیاز دارید اطلاعات رو session کاربر ذخیره کنید بهتره session ها server side ذخیره بشن 

server side session storage
در حالت خلاصه session server side جای اینکه اطلاعات رو در session در سمت کاربر ذخیره کنه میاد اطلاعات رو در سمت سرور ذخیره می کنه و به جاش یه ID منtحصر به فرد به کاربر میده (در session کاربر ذخیره میکنه ) و اطلاعات رو در سمت سرور توی فایل یا یه دیتابیس (mysql-redis-postgres , ...) ذخیره میکنه
و با هر بار درخواست کاربر میاد با توجه به ID کاربر اطلاعات رو از دیتابیس فراخوانی میکنه 

برای این کار میتونید از افزونه flask-session استفاده کنید. به علت اینکه این بحث طولانیه و خودش یه post دیگه می طلبه شمارو راهنمایی می کنم به داکیومنت flask-session برای کسب اطلاعات بیشتر
$ pip install flask-session
flask-session doc: 
https://flask-session.readthedocs.io/en/latest/




04.CSRF TOKEN PROTECATION
برای جلوگیری از اینکه درخواست غیرمجازی از سمت هکر ها به سمت سرور های ما (Flask Application) ارسال بشه باید از csrf token استفاده کنیم 


در یه تعریف انتزاعی و سطح بالا این توکن میاد صحت سنجی میکنه که درخواست از سمت کاربر اصلی ما ارسال شده و به طور فرعی یا غیرمستقیم ارسال نشده (خیلی ساده شده توضیح دادم ولی برای کسب اطلاعات بیشتر به این لینک برید)
کتابخونه های زیادی برای این کار وجود داره ولی یکی از معروف ترینشون کتابخونه flask-wtf هست که میاد این قابلیت رو به برنامه ما اضافه می کنه
ما ابتدا با دستور زیر این کتابخونه رو نصب می کنیم
$ pip install flask-wtf
و بعدش میاییم مثل هر کتابخونه دیگه فلسکی یه آبجکت از کلاس اصلیش می سازیم 
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config[SECRET_KEY] = os.urandom(24) or Secret key

# after configuration process
csrf = CSRFProtect(app=app)
با این کار به صورت خودکار این قابلیت به برنامه ما اضافه شد و حالا هر درخواست از نوع POST به سمت برنامه ما بیاد این افزونه اول چک میکنه که csrf token درسته یا نه و اگر درست بود اجازه میده درخواست به view برسه و انجام بشه در غیراین صورت ارور 400 برمیگردونه 

csrf error
برای  اضافه کردن csrf token به فرم هاتون میتونید از فرم های wtf استفاده کنید یا به صورت دستی به هر فرمی که داشتید بیایید یه input با type=Hidden و name=csrf_token بدید دقت کنید اسم باید دقیقا یکی باشه!
و بعد توی value اون input بیایید و فیلتر csrf_token رو صدا بزنید 




این input با هر بار درخواست یه مقدار تصادفی داره که برای هر کاربر متفاوته و سرور میاد این درخواست هارو بر اساس این مقدار صحت سنجی می کنه




05. Broken Authentication
بهتره برای احراز هویت کاربر از افزونه های سوم شخص (معتبر و رسمی) استفاده کنید و خودتون کل این فرایند رو پیاده سازی نکنید. چون هم گاهی یه سری edge case وجود داره که از زیر دستتون در میره و باعث باگ میشه و اینکه این فرایند نیازمند بروزرسانی های  دائم و دقیقی داره 
برای این فرایند میتونید از افزونه flask-login استفاده کنید و دوباره چون این افزونه دنیای خودش رو داره و نمیشه توی همین post کامل راجبش نوشته شمارو هدایت می کنم به داکیومنت رسمی flask-login
$ pip install flask-login
flask-login doc:
https://flask-login.readthedocs.io/en/latest/




06.Validate Inputs and Outputs
برای برنامه اتون ورودی و خروجی هارو حتما بررسی کنید و اعتبار سنجی کنید این ورودی ها میتونن شامل اطلاعات ذخیره شده در request باشند یا حتی اطلاعات ارسال شده از طریق form یا ...
که خود این مشکل میتونه باعت مشکلات اساسی مثل sql injection , xss ... میشه
برای این کار بهتره فرم هارو خودتون دستی نسازید و از کتابخونه هایی که برای این کار هستند استفاده کنید مثل flask-wtf برای ساخت فرم ها و flask-sqlachemy برای ارتباط با دیتابیس (CRUD)(ORM) و ...
اگه دوست دارید بیشتر راجب flask-sqlalchemy بدونید و بخونید این نوشته قبلی من رو یه سری بزنید 
https://vrgl.ir/wfO4E




07.Use the Latest Version of Flask
همیشه سعی کنید از آخرین ورژن بروز فلسک و افزونه هایی که استفاده می کنید استفاده کنید
 این یکی از مهم ترین شاخصه هاست. اصلا از نسخه های قدیمی یا Deprecate استفاده نکنید 
بعضی از برنامه از یه افزونه های خاصی استفاده می کنند که خیلی وقته که بروز نشدن در نتیجه با یه ورژن خاصی از فلسک سازگارن که معمولا قدیمیه و این بشدت خطرناکه 
برای همین همیشه بروز باشید و سعی کنید در بروزترین حالت ممکن باشه package هاتون






08.don't comment Sensitive information in templates
گاهی اوقات خیلی از افراد بی تجربه میان و توی template هاشون یه سری اطلاعات رو comment می کنند و فراموش می کنن که روی production این کامنت هارو حذف کنن و باعث ایجاد خیلی از مشکلات میشن 
+ حتی گاهی دیده شده که رمز دیتابیس رو هم توی template بوده :)
 پیشنهاد من اینکه که حد الامکان اصلا کامنتی چیزی ندازید چون بعدا یادتون میره حذفش کنید‌(هر چند ابزار هایی هم برای این مورد هست که کدتون رو review می کنه و اگر توکن یا چیز مهمی رو گزاشته باشید بین کد بهتون هشدار میده) ولی تجربه ثابت کرده که نکنید بهتره 
ولی اگر می کنید با استفاده از jinja این کارو کنید. خود فلسک برای هندل کردن template هاش از template engine jinja2 استفاده می کنه که قبل از این که هر template ای به سمت کاربر ارسال بشه اول به این engine داده میشه تا parse (یه جورایی انگار compile میکنه ولی در اصل میاد یه سری مقادیر رو جای گذاری میکنه و یه سری حلقه یا شرط هارو چک میکنه)‌ بشه و مقادیری یا هر کاری هست توش انجام بشه و بعد به سمت کاربر ارسال بشه
برای کامنت گذاشتن حداقلش با jinja کامنت بزارید چون هنگام parse کردن این کامنت هارو نادیده میگیره و ازشون رد میشه ولی در کد همچنان باقی میمونه (هر چند این روشم پیشنهاد نمیشه ولی خب :) )
برای کامنت گذاشتن توی خود html باید طبق زیر عمل کنیم :
<!-- Write your comments here -->
اما توی jinja باید طبق زیر عمل کنیم 
{# Write your comments here  #}
یعنی اگر توی کد ما طبق زیر کامنت بزارید و بعد با مرورگر صفحه رو ببینیم (source code ,   ctrl+U)

jinja and html comments
چیزی که در اصل می بینیم چیزی مثل زیره:

comments in html 
و همینطور که میبینم کامنتی که با jinja گزاشتیم به صورت خودکار از template حذف شده و بعد template به سمت کاربر ارسال شده




09.Use an ORM (Object–relational mapping)
برای ساخت جداول دیتابیس و عملیات های درج و ویرایش و ... بهتره از یه ORM استفاده بشه تا اینکه به صورت خام (raw) خودمون بین کدامون کد sql بنویسیم 
چون گاهی هکر ها از این وضعیت استفاده می کنن و کد های مخربی رو به فرم ما اضافه و ارسال می کنن که در عمل درسته مثال برای یه کوثری ساده که میخواییم یه کاربر رو توی دیتابیس جستجو کنیم یه چیزی مثل زیره در حالت عادی:
توجه: در مثال زیر حالاتی که بین دو تا  علامت % قرار دارند متغییر هستند و از معنی مستقلشون در sql جدا هستند 
 SELECT * FROM users WHERE username = '%username%' AND password = '%password%';
که برنامه ما میاد و username  و password رو جای این متغییر ها قرار میده و یه درخواست میزنه به دیتابیس 
اما اما اما یه هکری زرنگ میاد و داده رو طوری که ما میخواییم ارسال نمی کنه و این فرایند رو دور میزنه یا در اصل میپیچونه چجوری؟
میاد و مقادیری username  و password رو به صورت زیر برای ما ارسال میکنه 
username = 'admin --'
password = '   '
و برنامه ما درخواستی اصلی (query) رو به صورت زیر در نهایت به دست میاره
 SELECT * FROM users WHERE username = 'admin' -- AND password = ' ';
همینطور که میدونید علامت -- برای کامنت کردن در sql استفاده میشه یعنی عبارت بالا تنها یه درخواست میزنه و میبینه که آیا کاربری تحت نام کاربری admin هست یا نه و دیگه گذرواژه کاربر رو چک نمی کنه ;)

comment in sql
و به این صورت هکری میتونه به حساب کاربری ادمین وارد بشه. اما با استفاده از ORM ها ما جلوی این اتفاق رو می گیریم به صورت دیفالت (استفاده از ORM مزایای خیلی بیشتری نسبت به این داره و این تنها یکی از خوبیای استفاده از ORM هست)
چون در این رابطه یه نوشته کامل در ویرگول نوشتم زیاد نمی پردازم بهش اینجا و شمارو هدایت می کنم به اون نوشته از طریق این لینک
https://vrgl.ir/wfO4E






10. http security header
به صورت کلی مرورگر و کاربر با استفاده از http header ها یک سری اطلاعات رو بین خودشون انتقال میدن 
مثال برای اینکه سرور طول محتوای ارسالی رو به مرورگر بگه توی یه http header ای به اسم content-length میاد و این طول رو قرار میده و برای مرورگر ارسال میکنه(client)(صرفا مرورگر نه کلا هر برنامه یا کلاینتی که درخواست رو میزنه) یا مثلا برای اینکه سرور به کلاینت بگه نوع سند ارسالیش چیه اون رو توی یه http header خاصی به اسم Content-Type قرار میده 

virgool http headers
مثال اگر همین الان روی همین صفحه دکمه f12 رو بزنید و به تب Network برید و اولین درخواست رو باز کنید و به سربرگ headers برید میتونید http header هایی که سرور های ویرگول برای مرورگرتون ارسال کرده رو ببینید‌(در این مورد خاص چون ویرگول پشت CDN ابراروان هست یه بخشی از هدر ها توسط ابراروان تنظیم میشه )
مثال نوع برگشتی این سند از نوع text/html; charset=UTF-8 هست و اینکه تاریخ ارسال سند Tue, 20 Feb 2024 08:45:54 GMT هست و تاریخ انقضای این سند Tue, 20 Feb 2024 08:45:54 GMT هست 
و یا اینکه سروری که این پاسخ رو به من داده ArvanCloud هست (ابرآروان یه ارایه دهنده سرویس CDN در ایرانه )
ما یک سری http header استاندار داریم که تمام مرورگر ها اونها رو میفهنن و متوجه میشن که لیستش رو میتونید در این لینک بخونید 
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

security http headers 


اما یه سری هدر هم خود برنامه نویس به صورت اختیاری قرار میده و ارسال میکنه برای کلاینت (معمولا همون برنامه سمت کاربر که میشه react app یا vue و ...) که با x معمولا شروع میشه 
برای دیدن لیست تمام http security header ها میتونید به لینک زیر برید:
https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html
سخن نهایی
در انتها اینکه امنیت به طور کامل نیست و همیشه یه نقطه ای هست که از دست شما در رفته و امن نیست ولی شما باید تلاش کنید که همیشه بروز باشید :) 
امیدوارم این نوشته به دردتون بخوره و براتون مفید باشه اگر مشکلی یا سوالی هم داشتید میتونید توی قسمت کامنت ها برام بنویسید
 
راستی تمام کد این نوشته توی repo github زیر موجوده:
https://github.com/alisharify7/flask-security-tips




منابع مورد استفاده در این نوشته :
https://climbtheladder.com/10-flask-security-best-practices/
https://flask-login.readthedocs.io/en/latest/
https://portswigger.net/web-security/csrf
https://www.javatpoint.com/session-vs-cookies
https://medium.com/@tiff.sage/client-side-session-vs-server-side-session-d506f5408e8c
https://testdriven.io/tips/topics/flask
https://www.invicti.com/blog/web-security/http-security-headers/
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html

