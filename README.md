

---

## تمرین ۱: آماده‌سازی محیط پروژه

```bash
mkdir poject 
mkdir -p ~/project/{docs,templates,scripts,users,processes,network,backup,reports,tmp,archive}
cd ~/project
pwd
ls -l
tree
```
<div dir="rtl">
**توضیح:**
- `mkdir -p ~/project/{...}` یک پوشه اصلی به نام `project` در خانه کاربر می‌سازد و همزمان داخل آن، به کمک آکولاد `{}`، چند زیرپوشه (docs، templates، scripts، users، processes، network، backup، reports، tmp، archive) را در یک خط ایجاد می‌کند. فلگ `-p` باعث می‌شود اگر پوشه والد وجود نداشت، خودش ساخته شود و اگر پوشه از قبل بود، خطا ندهد.
- `cd ~/project` وارد پوشه پروژه می‌شویم تا بقیه کارها داخل همین مسیر انجام شود.
- `pwd` (Print Working Directory) مسیر کامل پوشه‌ای که الان داخلش هستیم را نشان می‌دهد؛ برای اثبات اینکه واقعاً داخل پوشه پروژه هستیم.
- `ls -l` محتویات پوشه را به‌صورت لیست کامل (با سطح دسترسی، مالک، اندازه و تاریخ) نشان می‌دهد.
- `tree` (اگر نصب نبود با `sudo apt install tree` نصبش کن) ساختار درختی کل پوشه‌ها و زیرپوشه‌ها را به‌صورت بصری و مرتب نشان می‌دهد؛ خیلی خوب برای اسکرین‌شات نهایی ساختار پروژه است.

---
</div>
## تمرین ۲: آشنایی با راهنمای دستورها

```bash
man ls
ls --help
whatis ls
info ls
apropos copy
```

**توضیح:**
- `man ls` صفحه راهنمای کامل (manual) دستور `ls` را باز می‌کند؛ شامل توضیح کلی، تمام گزینه‌ها (options) و نحوه استفاده. با `q` از آن خارج می‌شوی.
- `ls --help` یک خلاصه سریع‌تر و کوتاه‌تر از گزینه‌های دستور را مستقیم در ترمینال چاپ می‌کند، بدون باز شدن صفحه جدید.
- `whatis ls` فقط در یک خط توضیح می‌دهد که دستور `ls` چه کاری انجام می‌دهد.
- `info ls` نسخه تعاملی‌تر و گاهی مفصل‌تر از راهنما را باز می‌کند (فرمت GNU Info).
- `apropos copy` تمام دستوراتی که در توضیحاتشان کلمه "copy" وجود دارد را جستجو و لیست می‌کند؛ وقتی اسم دقیق دستور را نمی‌دانی مفید است.

برای گزارش، همین کار را برای چند دستور دیگر مثل `cp`, `chmod`, `find`, `ps` هم تکرار کن و در جدول بنویس.

---

## تمرین ۳: مدیریت مسیرها و پوشه‌ها

```bash
cd ~/project/docs
pwd
mkdir test_folder
mkdir -p test_folder/sub1/sub2
rmdir test_folder/sub1/sub2
ls
ls -a
ls -l
cd ..
cd ~/project
```

**توضیح:**
- `cd ~/project/docs` جابه‌جایی به داخل پوشه docs.
- `pwd` نمایش مسیر فعلی برای اطمینان از محل قرارگیری.
- `mkdir test_folder` ساخت یک پوشه آزمایشی.
- `mkdir -p test_folder/sub1/sub2` ساخت چند پوشه تو در تو در یک دستور (نیازی به ساخت مرحله‌به‌مرحله نیست).
- `rmdir test_folder/sub1/sub2` حذف یک پوشه خالی؛ توجه کن `rmdir` فقط پوشه‌های خالی را حذف می‌کند، اگر پوشه محتوا داشته باشد خطا می‌دهد.
- `ls` نمایش لیست ساده فایل‌ها و پوشه‌ها (فایل‌های مخفی که با نقطه شروع می‌شوند نشان داده نمی‌شوند).
- `ls -a` نمایش همه چیز شامل فایل‌های مخفی (که نامشان با `.` شروع می‌شود، مثل `.bashrc`).
- `ls -l` نمایش کامل (Long listing) شامل سطح دسترسی، تعداد لینک، مالک، گروه، اندازه فایل به بایت و تاریخ آخرین تغییر.
- `cd ..` بازگشت به یک پوشه بالاتر (پوشه والد).

**تفاوت نمایش معمولی و کامل:** `ls` فقط اسم‌ها را نشان می‌دهد ولی `ls -l` جزئیات کامل (سطح دسترسی، مالک، حجم، تاریخ) را هم می‌دهد که برای تحلیل بعدی (مثل بخش سطح دسترسی) لازم است.

---

## تمرین ۴: ساخت و مدیریت فایل‌های متنی

```bash
cd ~/project/docs
touch note1.txt note2.txt
echo "این خط اول است" > note1.txt
echo "این خط دوم است" >> note1.txt
cat note1.txt
nano note2.txt
cp note1.txt note1_copy.txt
mv note1_copy.txt note1_renamed.txt
mv note1_renamed.txt ~/project/tmp/
rm ~/project/tmp/note1_renamed.txt
```

**توضیح:**
- `touch note1.txt note2.txt` ساخت دو فایل خالی متنی. اگر فایل از قبل وجود داشته باشد فقط تاریخ آخرین تغییرش آپدیت می‌شود.
- `echo "متن" > note1.txt` نوشتن یک خط متن داخل فایل؛ علامت `>` محتوای قبلی فایل را کامل پاک کرده و متن جدید را جایگزین می‌کند (overwrite).
- `echo "متن" >> note1.txt` همان کار بالا ولی با دو تا `>>`؛ این بار متن جدید به **انتهای** فایل اضافه می‌شود بدون پاک کردن محتوای قبلی (append).
- `cat note1.txt` نمایش کامل محتوای فایل در ترمینال.
- `nano note2.txt` باز کردن ویرایشگر متنی nano برای نوشتن داخل فایل به‌صورت تعاملی (برای ذخیره: `Ctrl+O` سپس `Enter`، برای خروج: `Ctrl+X`).
- `cp note1.txt note1_copy.txt` کپی کردن یک فایل با نام جدید (فایل اصلی دست‌نخورده باقی می‌ماند).
- `mv note1_copy.txt note1_renamed.txt` تغییر نام فایل (دستور `mv` هم برای جابه‌جایی و هم برای تغییر نام استفاده می‌شود).
- `mv note1_renamed.txt ~/project/tmp/` انتقال فایل به پوشه دیگر.
- `rm ~/project/tmp/note1_renamed.txt` حذف فایل (این حذف دائمی است و به سطل بازیافت نمی‌رود، پس باید با احتیاط استفاده شود).

---

## تمرین ۵: هدایت خروجی و اتصال دستورها

```bash
cd ~/project/reports
ls -l ~/project > success_output.txt
ls -l ~/project/not_exist_folder 2> error_output.txt
ls -l ~/project >> success_output.txt
cat success_output.txt error_output.txt > combined_report.txt
ls ~/project | wc -l
ls ~/project | sort | head -5
```

**توضیح:**
- `ls -l ~/project > success_output.txt` خروجی موفق دستور (که به آن standard output یا stdout می‌گویند) داخل فایل ذخیره می‌شود (جایگزین محتوای قبلی).
- `ls -l ~/project/not_exist_folder 2> error_output.txt` چون این پوشه وجود ندارد، دستور خطا می‌دهد. علامت `2>` فقط پیام‌های خطا (standard error یا stderr) را در فایل جداگانه ذخیره می‌کند نه خروجی موفق را.
- `ls -l ~/project >> success_output.txt` این بار خروجی جدید به فایل قبلی **اضافه** می‌شود (append) بدون پاک کردن محتوای قبلی.
- `cat success_output.txt error_output.txt > combined_report.txt` محتوای دو فایل پشت‌سرهم خوانده و در یک فایل جدید ترکیبی ذخیره می‌شود.
- `ls ~/project | wc -l` علامت `|` (pipe) خروجی دستور اول را به‌عنوان ورودی دستور دوم می‌فرستد؛ یعنی خروجی `ls` به `wc -l` داده می‌شود که تعداد خطوط (در اینجا تعداد فایل/پوشه‌ها) را می‌شمارد.
- `ls ~/project | sort | head -5` یک زنجیره از سه دستور: لیست می‌گیرد، مرتب می‌کند، و فقط ۵ خط اول را نشان می‌دهد. این مثال خوبی از پردازش زنجیره‌ای است.

---

## تمرین ۶: ساخت و تحلیل فایل لاگ

```bash
cd ~/project/reports
cat > sample.log << EOF
INFO: سیستم راه‌اندازی شد
INFO: کاربر وارد شد
WARNING: فضای دیسک رو به اتمام است
ERROR: اتصال به شبکه قطع شد
INFO: عملیات ذخیره انجام شد
WARNING: دمای پردازنده باال است
ERROR: فایل پیدا نشد
EOF

grep "ERROR" sample.log
grep -c "ERROR" sample.log
grep -c "WARNING" sample.log
grep -c "INFO" sample.log
grep -n "ERROR" sample.log
```

**توضیح:**
- `cat > sample.log << EOF ... EOF` یک روش برای نوشتن چند خط متن مستقیم در فایل بدون باز کردن ویرایشگر (به این روش heredoc گفته می‌شود؛ هر چیزی بین دو `EOF` نوشته شود عیناً در فایل ذخیره می‌شود).
- `grep "ERROR" sample.log` تمام خطوطی که کلمه ERROR در آن‌ها وجود دارد را پیدا و نمایش می‌دهد.
- `grep -c "ERROR" sample.log` به‌جای نمایش خطوط، فقط **تعداد** خطوط مطابقت‌یافته را می‌شمارد (`-c` مخفف count).
- همین کار را برای WARNING و INFO هم انجام می‌دهیم تا آمار هر نوع پیام مشخص شود.
- `grep -n "ERROR" sample.log` علاوه بر نمایش خط، **شماره خط** آن را هم جلویش نشان می‌دهد؛ برای پیدا کردن دقیق محل خطا در فایل بزرگ مفید است.

---

## تمرین ۷: پردازش فایل‌های متنی

```bash
cd ~/project/reports
wc -l sample.log
wc -w sample.log
sort sample.log > sorted.log
sort sample.log | uniq > unique.log
cut -d ' ' -f1 sample.log
sed 's/ERROR/CRITICAL/g' sample.log > replaced.log
split -l 3 sample.log part_
```

**توضیح:**
- `wc -l sample.log` تعداد خطوط فایل را می‌شمارد (Word Count با گزینه lines).
- `wc -w sample.log` تعداد کلمات فایل را می‌شمارد.
- `sort sample.log > sorted.log` خطوط فایل را به ترتیب حروف الفبا مرتب کرده و در فایل جدید ذخیره می‌کند.
- `sort sample.log | uniq > unique.log` ابتدا مرتب‌سازی می‌شود (چون `uniq` فقط خطوط تکراری *پشت‌سرهم* را حذف می‌کند، پس نیاز به sort قبل از آن داریم)، سپس خطوط تکراری حذف می‌شوند.
- `cut -d ' ' -f1 sample.log` از هر خط، فقط بخش اول را (قبل از فاصله) جدا می‌کند؛ `-d ' '` یعنی جداکننده فاصله است و `-f1` یعنی فیلد شماره یک (مثلاً کلمه INFO یا ERROR در ابتدای هر خط).
- `sed 's/ERROR/CRITICAL/g' sample.log > replaced.log` دستور جایگزینی متن؛ هر کجا کلمه ERROR پیدا شود با CRITICAL جایگزین می‌شود (`s` یعنی substitute و `g` یعنی این کار در کل خط تکرار شود، نه فقط اولین مورد).
- `split -l 3 sample.log part_` فایل بزرگ را به چند فایل کوچک‌تر تقسیم می‌کند؛ اینجا هر فایل جدید ۳ خط دارد و اسم فایل‌ها با `part_` شروع می‌شود (مثلاً part_aa، part_ab).

---

## تمرین ۸: جستجوی فایل‌ها در پروژه

```bash
cd ~/project
find . -name "*.txt"
find . -name "*.log"
find . -type f
find . -type d
find . -empty
find . -size +1k
find . -perm -u+x
find . -name "*.log" -exec cp {} ~/project/archive/ \;
```

**توضیح:**
- `find . -name "*.txt"` جستجوی فایل‌ها بر اساس نام/پسوند، از پوشه فعلی (`.`) به بعد و در همه زیرپوشه‌ها؛ اینجا هر فایلی که پسوندش txt باشد را پیدا می‌کند.
- `find . -name "*.log"` مشابه بالا برای فایل‌های log.
- `find . -type f` فقط فایل‌ها را نشان می‌دهد (نه پوشه‌ها)؛ `f` یعنی file.
- `find . -type d` فقط پوشه‌ها را نشان می‌دهد؛ `d` یعنی directory.
- `find . -empty` فایل‌ها یا پوشه‌های خالی (بدون محتوا) را پیدا می‌کند.
- `find . -size +1k` فایل‌هایی که حجمشان بیشتر از ۱ کیلوبایت است را پیدا می‌کند.
- `find . -perm -u+x` فایل‌هایی که برای مالک (user) قابل اجرا (executable) هستند را پیدا می‌کند.
- `find . -name "*.log" -exec cp {} ~/project/archive/ \;` بعد از پیدا کردن فایل‌های log، روی هر کدام یک عملیات (اینجا کپی به پوشه archive) اجرا می‌کند؛ `{}` جای اسم فایل پیدا‌شده قرار می‌گیرد و `\;` پایان دستور exec را مشخص می‌کند.

---

## تمرین ۹: سطح دسترسی و مجوز فایل‌ها

```bash
cd ~/project/scripts
touch normal_file.txt
echo 'echo "سلام از اسکریپت"' > myscript.sh

ls -l normal_file.txt myscript.sh

./myscript.sh          # قبل از اجرایی کردن، خطای Permission denied می‌دهد

chmod +x myscript.sh
ls -l myscript.sh
./myscript.sh           # حالا اجرا می‌شود

chmod 644 normal_file.txt
chmod 400 normal_file.txt
chmod u+w,g-r,o-r normal_file.txt
```

**توضیح:**
- `touch normal_file.txt` و ساخت `myscript.sh` با یک خط کد ساده داخلش.
- `ls -l` قبل از تغییر، سطح دسترسی پیش‌فرض را نشان می‌دهد (معمولاً `-rw-r--r--` برای فایل معمولی).
- `./myscript.sh` تلاش برای اجرای اسکریپت؛ چون مجوز اجرا (execute) فعال نیست، خطای Permission denied می‌دهد.
- `chmod +x myscript.sh` اضافه کردن مجوز اجرا به فایل برای همه (owner, group, others).
- `ls -l myscript.sh` بعد از تغییر، حرف `x` در سطح دسترسی ظاهر می‌شود (مثلاً `-rwxr-xr-x`).
- `./myscript.sh` این‌بار اسکریپت با موفقیت اجرا شده و پیام را چاپ می‌کند.
- `chmod 644 normal_file.txt` تنظیم مجوز به روش عددی: 6 = خواندن+نوشتن برای مالک، 4 = فقط خواندن برای گروه، 4 = فقط خواندن برای دیگران.
- `chmod 400 normal_file.txt` فقط مالک اجازه خواندن دارد، هیچ‌کس دیگر حتی خواندن هم نمی‌تواند.
- `chmod u+w,g-r,o-r normal_file.txt` روش نمادین (symbolic): برای مالک (u) مجوز نوشتن اضافه می‌کند، از گروه (g) و دیگران (o) مجوز خواندن حذف می‌شود.

**مفهوم r/w/x:** `r` (read) یعنی توانایی خواندن محتوا، `w` (write) یعنی توانایی تغییر/نوشتن محتوا، `x` (execute) یعنی توانایی اجرا کردن فایل به‌عنوان برنامه/اسکریپت.

---

## تمرین ۱۰: مالکیت، گروه و مقدار پیش‌فرض مجوزها

```bash
cd ~/project/scripts
ls -l
umask
touch newfile_default.txt
ls -l newfile_default.txt

umask 022
touch test_umask1.txt
ls -l test_umask1.txt

umask 077
touch test_umask2.txt
ls -l test_umask2.txt

# فقط روی ماشین مجازی/محیط آزمایشگاهی:
sudo chown $USER:$USER newfile_default.txt
sudo chgrp sudo newfile_default.txt
```

**توضیح:**
- `ls -l` ستون‌های سوم و چهارم مالک (owner) و گروه (group) فایل را نشان می‌دهند.
- `umask` مقدار پیش‌فرض ماسک مجوز فعلی سیستم را نشان می‌دهد؛ این عدد تعیین می‌کند فایل‌های جدید با چه سطح دسترسی پیش‌فرضی ساخته شوند (معمولاً برای فایل‌ها پیش‌فرض ۶۶۶ منهای umask است).
- `touch newfile_default.txt` سپس `ls -l` روی آن، مجوز پیش‌فرض فایل تازه‌ساخته را نشان می‌دهد (بدون x چون فایل‌های معمولی به‌طور پیش‌فرض اجرایی نیستند).
- `umask 022` تغییر موقت مقدار umask؛ نتیجه‌اش این است که فایل‌های جدید مجوز `644` می‌گیرند.
- `umask 077` سخت‌گیرانه‌تر؛ فایل‌های جدید فقط برای مالک قابل خواندن/نوشتن خواهند بود (`600`) و گروه/دیگران هیچ دسترسی ندارند.
- `chown $USER:$USER file` تغییر مالک و گروه فایل به کاربر فعلی (`$USER` متغیر محیطی است که نام کاربر فعلی را نگه می‌دارد).
- `chgrp sudo file` تغییر فقط گروه فایل به یک گروه دیگر (اینجا گروه sudo به‌عنوان مثال؛ باید گروهی باشد که واقعاً در سیستم وجود دارد).

---

## تمرین ۱۱: لینک سخت و لینک نرم

```bash
cd ~/project/docs
echo "این فایل اصلی است" > original.txt

ln original.txt hardlink.txt
ln -s original.txt softlink.txt

ls -li original.txt hardlink.txt softlink.txt

echo "خط اضافه‌شده" >> original.txt
cat hardlink.txt
cat softlink.txt

rm original.txt
cat hardlink.txt     # محتوا هنوز موجود است
cat softlink.txt      # خطا می‌دهد چون فایل اصلی حذف شده
```

**توضیح:**
- `ln original.txt hardlink.txt` ساخت یک **لینک سخت (hard link)**؛ این یک اسم دیگر برای همان فایل روی دیسک است، نه یک فایل جدید. هر دو اسم به یک شناسه فایل (inode) اشاره می‌کنند.
- `ln -s original.txt softlink.txt` ساخت یک **لینک نرم/سمبلیک (symbolic link)**؛ این فقط یک اشاره‌گر (میانبر) به مسیر فایل اصلی است، شبیه شورتکات در ویندوز.
- `ls -li` گزینه `i` شماره inode هر فایل را نشان می‌دهد؛ خواهی دید که `original.txt` و `hardlink.txt` دقیقاً همان شماره inode را دارند (چون یک فایل هستند)، ولی `softlink.txt` شماره inode متفاوت دارد (چون خودش یک فایل جداست که فقط مسیر را نگه می‌دارد).
- وقتی به فایل اصلی چیزی اضافه می‌کنیم، هر دو لینک تغییر را نشان می‌دهند چون یا همان فایل هستند (hard link) یا به آن اشاره می‌کنند (soft link).
- بعد از `rm original.txt`: لینک سخت هنوز کار می‌کند و محتوا در دسترس است، چون فایل واقعی تا وقتی حداقل یک لینک سخت به آن اشاره کند حذف نمی‌شود؛ اما لینک نرم "شکسته" (broken) می‌شود چون مسیری که به آن اشاره می‌کرد دیگر وجود ندارد.

---

## تمرین ۱۲: فشرده‌سازی، آرشیو و بازیابی

```bash
cd ~/project
tar -cvf backup/project_archive.tar docs templates scripts
tar -tvf backup/project_archive.tar
gzip -k backup/project_archive.tar
ls -l backup/

mkdir -p archive/restore_test
tar -xvf backup/project_archive.tar -C archive/restore_test
ls -R archive/restore_test
```

**توضیح:**
- `tar -cvf backup/project_archive.tar docs templates scripts` ساخت یک فایل آرشیو (بدون فشرده‌سازی) از چند پوشه؛ `c` یعنی create، `v` یعنی verbose (نمایش لیست فایل‌ها حین کار)، `f` یعنی مشخص کردن اسم فایل خروجی.
- `tar -tvf backup/project_archive.tar` نمایش محتویات آرشیو **بدون استخراج کردن** آن؛ `t` یعنی list.
- `gzip -k backup/project_archive.tar` فشرده کردن فایل آرشیو با فرمت gzip؛ فایل `project_archive.tar.gz` ساخته می‌شود. گزینه `-k` (keep) باعث می‌شود فایل tar اصلی هم حذف نشود.
- `ls -l backup/` مقایسه حجم فایل tar و tar.gz برای دیدن میزان فشرده‌سازی.
- `mkdir -p archive/restore_test` ساخت پوشه‌ای جداگانه برای بازیابی (تا با فایل‌های اصلی قاطی نشود).
- `tar -xvf backup/project_archive.tar -C archive/restore_test` استخراج (extract) محتویات آرشیو داخل پوشه مشخص‌شده؛ `x` یعنی extract و `-C` مسیر مقصد را تعیین می‌کند.
- `ls -R archive/restore_test` نمایش بازگشتی (Recursive) کل ساختار بازیابی‌شده برای اطمینان از صحت آن.

---

## تمرین ۱۳: بررسی اطلاعات سیستم

```bash
whoami
hostname
uname -a
uptime
lscpu
free -h
df -h
lsblk
lsusb
```

**توضیح:**
- `whoami` نمایش نام کاربری که در حال حاضر لاگین است.
- `hostname` نمایش نام دستگاه/سیستم روی شبکه.
- `uname -a` نمایش کامل اطلاعات کرنل و سیستم‌عامل شامل نسخه کرنل، معماری (مثل x86_64) و تاریخ کامپایل.
- `uptime` نشان می‌دهد سیستم چه مدت است روشن است، چند کاربر متصل‌اند و میانگین بار پردازشی (load average) سیستم.
- `lscpu` اطلاعات کامل پردازنده شامل تعداد هسته‌ها، معماری و فرکانس.
- `free -h` نمایش وضعیت حافظه RAM و فضای swap به‌صورت خوانا (`-h` یعنی human-readable، یعنی به‌جای بایت، مگابایت/گیگابایت نشان می‌دهد).
- `df -h` نمایش فضای اشغال‌شده و آزاد دیسک‌ها/پارتیشن‌ها به‌صورت خوانا.
- `lsblk` نمایش ساختار درختی دیسک‌ها و پارتیشن‌های متصل به سیستم.
- `lsusb` نمایش دستگاه‌های متصل از طریق پورت USB.

**تحلیل کوتاه در گزارش:** بنویس چند درصد از RAM و دیسک استفاده شده و آیا سیستم در وضعیت سالمی است یا نزدیک به پر شدن.

---

## تمرین ۱۴: مدیریت فرآیندها

```bash
ps aux
ps aux | grep bash

sleep 100 &
jobs
ps aux | grep sleep

pid=$(pgrep -n sleep)
echo $pid
ps -p $pid

kill $pid
ps aux | grep sleep
```

**توضیح:**
- `ps aux` نمایش تمام فرآیندهای در حال اجرا روی سیستم با جزئیات (کاربر، PID، درصد استفاده CPU/حافظه، دستور اجراشده).
- `ps aux | grep bash` فیلتر کردن خروجی بالا فقط برای فرآیندهایی که اسمشان شامل bash است.
- `sleep 100 &` اجرای دستور sleep (که ۱۰۰ ثانیه صبر می‌کند) در **پس‌زمینه**؛ علامت `&` باعث می‌شود ترمینال بلاک نشود و بلافاصله کنترل به کاربر برگردد.
- `jobs` نمایش لیست کارهای در حال اجرا در پس‌زمینه در همین نشست ترمینال.
- `pid=$(pgrep -n sleep)` پیدا کردن شناسه فرآیند (PID) آخرین پردازش sleep و ذخیره آن در متغیر `pid`.
- `ps -p $pid` نمایش وضعیت دقیق همان فرآیند با شناسه پیدا‌شده.
- `kill $pid` ارسال سیگنال پیش‌فرض (SIGTERM) برای خاتمه کنترل‌شده فرآیند.
- بعد از kill، دوباره `ps aux | grep sleep` نشان می‌دهد که فرآیند دیگر وجود ندارد.

---

## تمرین ۱۵: اولویت و زمان اجرای فرآیندها

```bash
nice -n 10 sleep 60 &
ps -o pid,ni,cmd -p $(pgrep -n sleep)

renice -n 5 -p $(pgrep -n sleep)
ps -o pid,ni,cmd -p $(pgrep -n sleep)

time ls -R ~/project
```

**توضیح:**
- `nice -n 10 sleep 60 &` اجرای یک فرآیند با اولویت پایین‌تر از حالت عادی در پس‌زمینه. مقدار nice از -20 (بالاترین اولویت) تا 19 (پایین‌ترین اولویت) متغیر است؛ عدد بزرگ‌تر یعنی فرآیند "مهربان‌تر" است و منابع کمتری از CPU می‌خواهد.
- `ps -o pid,ni,cmd -p $(pgrep -n sleep)` نمایش ستون‌های دلخواه (شناسه فرآیند، مقدار nice، و دستور) فقط برای همان فرآیند.
- `renice -n 5 -p $(pgrep -n sleep)` تغییر اولویت یک فرآیند در حال اجرا (بدون نیاز به کشتن و اجرای دوباره‌اش) به مقدار جدید.
- دوباره چک کردن با `ps -o` برای دیدن مقدار nice تغییریافته.
- `time ls -R ~/project` اندازه‌گیری زمان اجرای یک دستور؛ خروجی شامل سه مقدار است: `real` (زمان واقعی سپری‌شده)، `user` (زمان CPU در حالت کاربر) و `sys` (زمان CPU در حالت سیستم).

---

## تمرین ۱۶: کاربران و گروه‌ها

```bash
whoami
id
groups
who
last -n 5

# فقط روی ماشین مجازی/محیط آزمایشگاهی:
sudo groupadd testgroup
sudo useradd -m -G testgroup testuser
id testuser
groups testuser

sudo userdel -r testuser
sudo groupdel testgroup
```

**توضیح:**
- `whoami` نمایش نام کاربر فعلی.
- `id` نمایش شناسه کاربری (UID)، شناسه گروه اصلی (GID) و تمام گروه‌هایی که کاربر عضو آن‌هاست.
- `groups` نمایش اسم گروه‌هایی که کاربر فعلی عضو آن‌هاست.
- `who` نمایش کاربرانی که در حال حاضر به سیستم لاگین هستند.
- `last -n 5` نمایش ۵ مورد آخر از تاریخچه ورود کاربران به سیستم.
- `sudo groupadd testgroup` ساخت یک گروه آزمایشی جدید (نیاز به دسترسی root دارد، برای همین `sudo`).
- `sudo useradd -m -G testgroup testuser` ساخت یک کاربر آزمایشی جدید؛ `-m` یعنی پوشه home برایش ساخته شود و `-G testgroup` یعنی این کاربر به گروه testgroup اضافه شود.
- `id testuser` و `groups testuser` بررسی اینکه کاربر جدید واقعاً عضو گروه شده است.
- `sudo userdel -r testuser` حذف کاربر آزمایشی همراه با پوشه home او (`-r` یعنی remove home directory).
- `sudo groupdel testgroup` حذف گروه آزمایشی.

⚠️ این بخش را فقط روی ماشین مجازی انجام بده، نه روی سیستم اصلی خودت.

---

## تمرین ۱۷: سرویس‌ها و لاگ‌های سیستمی

```bash
systemctl status ssh
systemctl list-units --type=service --state=running
journalctl -u ssh -n 20

# فقط با دسترسی و در محیط آزمایشگاهی:
sudo systemctl stop ssh
systemctl status ssh
sudo systemctl start ssh
systemctl status ssh
```

**توضیح:**
- `systemctl status ssh` نمایش وضعیت فعلی یک سرویس مشخص (اینجا ssh)؛ نشان می‌دهد فعال است یا نه، از چه زمانی در حال اجراست و چند خط آخر لاگ آن.
- `systemctl list-units --type=service --state=running` نمایش لیست همه سرویس‌هایی که هم‌اکنون در حال اجرا هستند.
- `journalctl -u ssh -n 20` نمایش ۲۰ خط آخر از لاگ‌های سیستمی مربوط به سرویس ssh؛ `-u` یعنی unit (واحد سرویس) و این دستور برای بررسی رفتار یا خطاهای اخیر یک سرویس خیلی کاربردی است.
- `sudo systemctl stop ssh` متوقف کردن موقت سرویس (نیاز به دسترسی ادمین).
- `sudo systemctl start ssh` راه‌اندازی مجدد سرویس متوقف‌شده.
- بین این دو دستور، با `systemctl status ssh` تغییر وضعیت (inactive به active) را می‌بینی و می‌توانی اسکرین‌شات بگیری.

اگر ssh روی سیستمت نصب نیست، می‌توانی از سرویس دیگری مثل `cron` یا `cups` به‌جایش استفاده کنی.

---

## تمرین ۱۸: مدیریت بسته‌ها و ابزارها

```bash
apt search tree
apt show tree
sudo apt install tree
tree --version
sudo apt remove tree
```

**توضیح:**
- `apt search tree` جستجوی یک بسته نرم‌افزاری کم‌حجم و بی‌خطر (اینجا ابزار `tree` که ساختار پوشه‌ها را نمایش می‌دهد) در مخزن نرم‌افزاری سیستم.
- `apt show tree` نمایش اطلاعات کامل بسته شامل توضیح، نسخه، حجم و وابستگی‌ها، قبل از نصب.
- `sudo apt install tree` نصب واقعی بسته روی سیستم (نیاز به دسترسی ادمین).
- `tree --version` بررسی اینکه ابزار درست نصب شده و نسخه‌اش را نشان دادن.
- `sudo apt remove tree` حذف بسته از سیستم در صورت نیاز.

---

## تمرین ۱۹: بررسی شبکه

```bash
cd ~/project/network

ip a > ip_info.txt
ip route > route_info.txt

ping -c 4 8.8.8.8 > ping_result.txt

ss -tuln > open_ports.txt

curl -I https://www.google.com > http_request.txt

cat ip_info.txt route_info.txt ping_result.txt open_ports.txt http_request.txt
```

**توضیح:**
- `ip a` (یا `ip addr`) نمایش تمام رابط‌های شبکه (interfaces) سیستم و نشانی IP اختصاص‌یافته به هرکدام.
- `ip route` نمایش جدول مسیریابی، از جمله مسیر پیش‌فرض (default gateway) که ترافیک خروجی از آن عبور می‌کند.
- `ping -c 4 8.8.8.8` ارسال ۴ بسته آزمایشی به یک سرور مشخص (اینجا DNS گوگل) برای بررسی اتصال به اینترنت و زمان پاسخ (latency)؛ `-c 4` یعنی فقط ۴ بار تست کند و متوقف شود.
- `ss -tuln` نمایش درگاه‌های (ports) باز و در حال گوش‌دادن (listening) روی سیستم؛ `t` یعنی TCP، `u` یعنی UDP، `l` یعنی listening و `n` یعنی نمایش شماره پورت به‌جای اسم سرویس.
- `curl -I https://www.google.com` ارسال یک درخواست ساده HTTP و دریافت فقط هدر پاسخ (بدون محتوای کامل صفحه)؛ برای تست دسترسی به یک وب‌سایت خاص مفید است.
- در پایان، محتوای همه فایل‌های گزارش را با `cat` کنار هم می‌بینیم و یک تحلیل کوتاه در گزارش می‌نویسیم (مثلاً: آیا پینگ موفق بود؟ چند پورت باز است؟).

---

## تمرین ۲۰: متغیرهای محیطی و رفتار Shell

```bash
env
echo $HOME
echo $PATH

MY_VAR="سلام دنیا"
echo $MY_VAR
export MY_VAR
bash -c 'echo $MY_VAR'
unset MY_VAR
echo $MY_VAR

read -p "اسم خود را وارد کنید: " name
echo "سلام $name"

if [ "$name" == "ali" ]; then
  echo "خوش آمدی علی"
else
  echo "کاربر ناشناس"
fi
```

**توضیح:**
- `env` نمایش تمام متغیرهای محیطی (environment variables) فعلی سیستم.
- `echo $HOME` و `echo $PATH` نمونه‌ای از متغیرهای محیطی مهم؛ `HOME` مسیر پوشه خانه کاربر و `PATH` لیست مسیرهایی است که سیستم برای پیدا کردن دستورهای اجرایی در آن‌ها جستجو می‌کند.
- `MY_VAR="سلام دنیا"` ساخت یک متغیر موقت محلی (فقط در همین نشست ترمینال معتبر است).
- `echo $MY_VAR` نمایش مقدار متغیر (علامت `$` قبل از اسم متغیر برای خواندن مقدارش لازم است).
- `export MY_VAR` این متغیر محلی را به یک متغیر محیطی تبدیل می‌کند که به زیرفرآیندها (subprocesses) هم منتقل می‌شود؛ برای همین در `bash -c '...'` (که یک shell جدید باز می‌کند) هم قابل مشاهده است.
- `unset MY_VAR` حذف کامل متغیر از حافظه.
- `read -p "..." name` دریافت ورودی از کاربر و ذخیره آن در متغیر `name`؛ `-p` یعنی نمایش یک پیام راهنما قبل از دریافت ورودی.
- بلوک `if [ "$name" == "ali" ]; then ... else ... fi` یک شرط ساده است: اگر مقدار وارد‌شده برابر "ali" باشد پیام خوش‌آمدگویی خاص چاپ می‌شود، در غیر این صورت پیام عمومی.

---

## تمرین ۲۱: نوشتن اسکریپت گزارش نهایی

```bash
nano ~/project/scripts/final_report.sh
```

محتوای فایل `final_report.sh`:

```bash
#!/bin/bash

REPORT=~/project/reports/final_report_$(date +%Y%m%d_%H%M%S).txt

echo "=== گزارش نهایی سیستم ===" > "$REPORT"
echo "تاریخ: $(date)" >> "$REPORT"
echo "کاربر: $(whoami)" >> "$REPORT"
echo "نام سیستم: $(hostname)" >> "$REPORT"
echo "کرنل: $(uname -r)" >> "$REPORT"

echo -e "\n--- حافظه ---" >> "$REPORT"
free -h >> "$REPORT"

echo -e "\n--- دیسک ---" >> "$REPORT"
df -h >> "$REPORT"

echo -e "\n--- فایل‌های پروژه ---" >> "$REPORT"
find ~/project -type f | wc -l >> "$REPORT"

echo -e "\n--- فرآیندهای فعال (10 مورد اول) ---" >> "$REPORT"
ps aux --sort=-%cpu | head -n 10 >> "$REPORT"

echo -e "\n--- اطلاعات شبکه ---" >> "$REPORT"
ip a >> "$REPORT"

echo -e "\n--- خالصه لاگ‌ها ---" >> "$REPORT"
grep -c "ERROR" ~/project/reports/sample.log >> "$REPORT"

echo -e "\n--- وضعیت پشتیبان ---" >> "$REPORT"
ls -l ~/project/backup >> "$REPORT"

echo "گزارش با موفقیت ساخته شد: $REPORT"
```

سپس اجرا:

```bash
chmod +x ~/project/scripts/final_report.sh
~/project/scripts/final_report.sh
cat ~/project/reports/final_report_*.txt
```

**توضیح:**
- خط اول `#!/bin/bash` به آن shebang می‌گویند و مشخص می‌کند این فایل باید با bash اجرا شود.
- `REPORT=~/project/reports/final_report_$(date +%Y%m%d_%H%M%S).txt` ساخت یک اسم فایل یکتا با استفاده از تاریخ و زمان فعلی، تا هر بار اجرای اسکریپت، فایل قبلی را پاک نکند.
- هر بخش از اسکریپت با `>>` (append) اطلاعات مربوط به یک موضوع خاص (کاربر، حافظه، دیسک، فرآیندها، شبکه، لاگ، پشتیبان) را به فایل گزارش اضافه می‌کند.
- `$(...)` یعنی خروجی یک دستور را داخل رشته دیگر جاسازی کن (command substitution)، مثل `$(date)` که تاریخ فعلی را می‌گیرد.
- `chmod +x` فایل را قابل اجرا می‌کند، سپس با `./final_report.sh` یا مسیر کامل آن را اجرا می‌کنیم.
- در نهایت با `cat` محتوای گزارش تولیدشده را می‌بینیم.

---

## تمرین ۲۲: زمان‌بندی اجرای یک کار

**روش ۱ - با crontab (زمان‌بندی تکرارشونده):**
```bash
crontab -e
```
داخل فایل باز شده این خط را اضافه کن (اجرا هر روز ساعت ۹ صبح):
```
0 9 * * * /home/YOUR_USERNAME/project/scripts/final_report.sh
```
سپس بررسی:
```bash
crontab -l
```

**روش ۲ - با at (زمان‌بندی یک‌باره، ساده‌تر برای تست):**
```bash
sudo apt install at
echo "~/project/scripts/final_report.sh" | at now + 1 minute
atq
```

**توضیح:**
- `crontab -e` باز کردن فایل زمان‌بندی کارهای دوره‌ای کاربر فعلی برای ویرایش.
- ساختار خط cron شامل پنج فیلد زمانی (دقیقه، ساعت، روز ماه، ماه، روز هفته) و بعد از آن مسیر دستور/اسکریپت است؛ `0 9 * * *` یعنی دقیقه صفر، ساعت ۹، هر روز.
- `crontab -l` نمایش لیست کارهای زمان‌بندی‌شده فعلی برای بررسی صحت ثبت.
- `at now + 1 minute` روش ساده‌تر برای زمان‌بندی یک اجرای **یک‌باره** (نه تکراری) که یک دقیقه بعد اجرا می‌شود؛ برای تست سریع‌تر و گرفتن اسکرین‌شات مناسب‌تر است چون نیازی به صبر طولانی نیست.
- `atq` نمایش لیست کارهای زمان‌بندی‌شده در صف at.
- بعد از گذشت زمان تعیین‌شده، با چک کردن پوشه reports (مثلاً `ls -lt ~/project/reports`) می‌توانی ببینی فایل گزارش جدید در زمان درست ساخته شده است.

---

## تمرین ۲۳: پشتیبان‌گیری مرحله‌ای و مقایسه

```bash
mkdir -p ~/project/backup/stage1
cp -r ~/project/docs ~/project/scripts ~/project/backup/stage1/

echo "این یک تغییر جدید است" >> ~/project/docs/note1.txt

mkdir -p ~/project/backup/stage2
cp -r ~/project/docs ~/project/scripts ~/project/backup/stage2/

diff ~/project/backup/stage1/docs/note1.txt ~/project/backup/stage2/docs/note1.txt

# روش بهتر و حرفه‌ای‌تر با rsync (فقط تغییرات را کپی می‌کند):
rsync -av --progress ~/project/docs ~/project/backup/stage2_rsync/
```

**توضیح:**
- `cp -r` کپی بازگشتی (recursive) یک پوشه همراه با تمام محتویاتش، برای گرفتن نسخه پشتیبان مرحله اول (stage1).
- بعد از این، یک تغییر کوچک عمداً در یکی از فایل‌ها ایجاد می‌کنیم تا تفاوت بین نسخه‌ها قابل مشاهده باشد.
- دوباره `cp -r` برای گرفتن نسخه پشتیبان دوم (stage2) بعد از تغییر.
- `diff file1 file2` مقایسه محتوای دو فایل خط‌به‌خط و نمایش دقیق تفاوت‌ها (خطوطی که اضافه یا حذف شده‌اند).
- `rsync -av --progress source destination` ابزار حرفه‌ای‌تر برای پشتیبان‌گیری؛ برخلاف `cp` که هر بار همه‌چیز را از نو کپی می‌کند، `rsync` فقط فایل‌های تغییر‌کرده یا جدید را منتقل می‌کند که برای پشتیبان‌گیری‌های بعدی سریع‌تر است. `-a` یعنی حالت آرشیو (حفظ مجوزها و تاریخ‌ها) و `-v` یعنی نمایش جزئیات (verbose).

**مقایسه اجرای اول و دوم:** در گزارش بنویس که اجرای اول یک کپی کامل از حالت اولیه بود، ولی اجرای دوم شامل تغییر جدید هم بود و با `diff` می‌توان دقیقاً همان خط تغییریافته را دید.

---

## تمرین ۲۴: پاک‌سازی کنترل‌شده پروژه

```bash
cd ~/project/tmp
touch temp1.tmp temp2.tmp temp3.tmp cache_test.tmp
ls -l ~/project/tmp

find ~/project/tmp -name "*.tmp" -type f
find ~/project/tmp -name "*.tmp" -type f -delete

ls -l ~/project/tmp
tree ~/project
```

**توضیح:**
- ساخت چند فایل موقت آزمایشی با پسوند مشخص (`.tmp`) داخل پوشه `tmp` که از قبل برای همین منظور ساخته بودیم.
- `ls -l` قبل از پاک‌سازی، برای مستند کردن وضعیت اولیه (این خروجی را در گزارش به‌عنوان "قبل" قرار بده).
- `find ~/project/tmp -name "*.tmp" -type f` ابتدا فقط برای دیدن لیست فایل‌هایی که قرار است حذف شوند (بدون حذف واقعی) - این یک اقدام احتیاطی خوب قبل از هر حذف است.
- `find ~/project/tmp -name "*.tmp" -type f -delete` حذف **فقط** فایل‌هایی که پسوند `.tmp` دارند و در پوشه tmp هستند؛ این روش امن‌تر از `rm -rf` است چون معیار دقیق (نام، نوع، مسیر) مشخص شده و امکان حذف اشتباه فایل‌های اصلی پروژه وجود ندارد.
- `ls -l` و `tree` بعد از پاک‌سازی، برای اثبات اینکه فقط فایل‌های موقت حذف شدند و بقیه پوشه‌های پروژه (docs، scripts و...) دست‌نخورده باقی مانده‌اند.

**معیار حذف:** فقط فایل‌هایی حذف شدند که هم پسوندشان `.tmp` بود و هم داخل پوشه مخصوص فایل‌های موقت قرار داشتند؛ به این ترتیب خطر حذف تصادفی فایل‌های اصلی پروژه از بین می‌رود.

---

## تمرین ۲۵ (اختیاری): برنامه فرآیندی کوچک

می‌توانی این کار را با یک اسکریپت ساده bash انجام دهی (نیازی به زبان C نیست):

```bash
nano ~/project/scripts/proc_info.sh
```

محتوای فایل:
```bash
#!/bin/bash
echo "PID فرآیند فعلی: $$"
echo "PID فرآیند والد: $PPID"
echo "در حال اجرا برای ۱۰ ثانیه..."
sleep 10
echo "پایان اجرا"
```

اجرا:
```bash
chmod +x ~/project/scripts/proc_info.sh
~/project/scripts/proc_info.sh &
ps -o pid,ppid,cmd -p $!
wait
```

**توضیح:**
- `$$` یک متغیر خاص در bash است که شناسه فرآیند (PID) خودِ اسکریپت در حال اجرا را نگه می‌دارد.
- `$PPID` شناسه فرآیند والد (parent) را نشان می‌دهد؛ یعنی فرآیندی که این اسکریپت را صدا زده (مثلاً خود شل ترمینال).
- `sleep 10` باعث می‌شود اسکریپت ۱۰ ثانیه فعال/زنده بماند تا فرصت کافی برای بررسی وضعیتش از یک ترمینال دیگر وجود داشته باشد.
- با اجرای `proc_info.sh &` در پس‌زمینه، `$!` شناسه فرآیند آخرین کاری که در پس‌زمینه اجرا شده را نگه می‌دارد.
- `ps -o pid,ppid,cmd -p $!` نمایش اطلاعات همان فرآیند از دید سیستم، برای مقایسه با چیزی که خودِ اسکریپت چاپ کرده بود.
- `wait` منتظر می‌ماند تا فرآیند پس‌زمینه کامل تمام شود قبل از ادامه ترمینال.

---

## نکات پایانی برای گزارش

برای هر تمرین بالا، این ساختار را در گزارش رعایت کن:
1. عنوان و هدف تمرین
2. دستورهایی که اجرا کردی (دقیقاً همان‌هایی که تایپ کردی)
3. اسکرین‌شات خروجی ترمینال
4. یک یا دو خط توضیح "این خروجی یعنی چه"
5. اگر مشکلی پیش آمد، چطور حلش کردی

در نتیجه‌گیری نهایی هم بنویس که ترمینال لینوکس چطور یک ابزار یکپارچه برای مدیریت فایل، فرآیند، کاربر، شبکه و منابع سیستم است و کدام بخش (مثلاً سطح دسترسی یا مدیریت فرآیندها) برایت سخت‌تر یا جالب‌تر بود.


