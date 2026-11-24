import os
os.makedirs('css',exist_ok=True); os.makedirs('js',exist_ok=True)
CATS={'toner':('Тонер',[('Хөвөн тонер 200мл',32000),('AHA/BHA тонер',38000),('Чийгшүүлэх тонер',29000),('Тонер жийргэвч 60ш',45000)]),
'serum':('Серум, Ампул',[('Серум C витамин',65000),('Ампул гиалурон',58000),('Ретинол серум',72000),('Ниацинамид ампул',49000)]),
'cream':('Чийгшүүлэх тос',[('Чийгшүүлэгч тос 50мл',38000),('Нүдний тос',42000),('Шөнийн тос',55000),('Нарнаас хамгаалах тос SPF50',34000)]),
'mask':('Маск',[('Нүүрний хавтан маск 10ш',25000),('Шавар маск',31000),('Шөнийн маск',36000),('Уруулын маск',18000)]),
'makeup':('Make up',[('Тональ тос',48000),('Уруулын будаг',28000),('Сормуусны гоёл',25000),('Нүдний сүүдэр палитр',56000)]),
'device':('Төхөөрөмж',[('Нүүр массажны багаж',78000),('LED маск төхөөрөмж',320000),('Ультрадуун цэвэрлэгч',95000),('Гэрэлтэй толь',64000)]),
'hairbody':('Үс, Бие арчилгаа',[('Шампунь 400мл',18000),('Үсний маск',32000),('Биеийн лосьон',26000),('Шүршүүрийн гель',14000)]),
'sun':('Нарнаас хамгаалах',[('Sun cream SPF50+',34000),('Sun stick',29000),('Sun cushion',42000),('Нарны дараах гель',22000)])}
def page(fn,title,body):
    sub=[('cat-cream.html','Арьс арчилгаа'),('cat-device.html','Төхөөрөмж'),('cat-mask.html','Маск'),('cheap.html','50,000₮-с доош'),('sale.html','Sale %'),('bestseller.html','Best Seller')]
    subnav=''.join(f'<a href="{h}">{t}</a>' for h,t in sub)
    cats=''.join(f'<li><a class="dropdown-item" href="cat-{k}.html">{v[0]}</a></li>' for k,v in CATS.items())
    html=f'''<!DOCTYPE html>
<html lang="mn"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Гоо Зүйл</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="css/style.css"></head><body>
<!-- ===== МАСТЕР ХУУДАС: header ===== -->
<header class="top border-bottom bg-white sticky-top"><div class="container d-flex align-items-center py-2 gap-3">
<a class="logo" href="index.html">GOO ZUIL</a>
<form class="flex-grow-1 d-none d-md-flex" action="search.html"><input class="form-control" name="q" placeholder="Бүтээгдэхүүн хайх"><button class="btn btn-brand ms-2">Хайх</button></form>
<select class="form-select form-select-sm w-auto"><option>Монгол</option><option>English</option><option>中文</option></select>
<a class="small text-dark" href="login.html">Нэвтрэх</a><a class="small text-dark" href="account.html">Хэтэвч</a>
<a class="btn btn-outline-dark btn-sm" href="cart.html">Сагслах <span id="cartCount" class="badge bg-dark">0</span></a></div>
<nav class="subnav"><div class="container"><div class="dropdown d-inline"><a class="dropdown-toggle" data-bs-toggle="dropdown" href="#">Бүх ангилал</a><ul class="dropdown-menu">{cats}</ul></div>{subnav}</div></nav></header>
<main class="container py-4">{body}</main>
<!-- ===== МАСТЕР ХУУДАС: footer ===== -->
<footer class="bg-dark text-light pt-4 pb-3 mt-5"><div class="container">
<div class="row g-3"><div class="col-md-3"><h6>GOO ZUIL</h6><a class="d-block small" href="survey.html">Хэрэглэгчийн судалгаа</a><a class="d-block small" href="about.html">Бидний тухай</a><a class="d-block small" href="location.html">Хаяг байршил</a><a class="d-block small" href="contact.html">Санал хүсэлт</a></div>
<div class="col-md-3"><h6>Хэрэглэгчийн туслах</h6><a class="d-block small" href="policy.html">Нууцлалын бодлого</a><a class="d-block small" href="return.html">Буцаалтын журам</a><a class="d-block small" href="help.html">Түгээмэл асуулт, хариулт</a><a class="d-block small" href="terms.html">Үйлчилгээний нөхцөл</a></div>
<div class="col-md-3"><h6>Холбоо барих</h6><p class="small mb-0">И-Мэйл: info@goozuil.mn<br>Утас: 7700-0000<br>Хаяг: Сүхбаатар дүүрэг, 1-р хороо, Улаанбаатар</p></div>
<div class="col-md-3"><h6>Шинэчлэлт, мэдээ авах</h6><form id="subForm" class="d-flex"><input class="form-control form-control-sm" type="email" placeholder="Имэйл" required><button class="btn btn-sm btn-brand ms-1">Бүртгүүлэх</button></form></div></div>
<p class="small text-center mt-3 mb-0">© 2026. Бүх эрх хуулиар хамгаалагдсан.</p></div></footer>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="js/main.js"></script></body></html>'''
    open(fn,'w',encoding='utf-8').write(html)
def card(k,i,n,p):
    return f'''<div class="col-6 col-md-3"><div class="card h-100 product"><div class="ph">{n[0]}</div><div class="card-body">
<h6><a href="product-{k}.html" class="text-decoration-none">{n}</a></h6><p class="price">{p:,}₮</p>
<button class="btn btn-sm btn-brand add" data-name="{n}" data-price="{p}">Сагсанд нэмэх</button></div></div></div>'''
# 1 index
ct=''.join(f'<div class="col-6 col-md-3"><a class="catbox" href="cat-{k}.html">{v[0]}</a></div>' for k,v in CATS.items())
best=''.join(card(k,0,*v[1][0]) for k,v in list(CATS.items())[:4])
page('index.html','Нүүр','''<div id="slide" class="carousel slide mb-4" data-bs-ride="carousel"><div class="carousel-inner">
<div class="carousel-item active"><div class="banner b1">Өвлийн арчилгаа -30%</div></div>
<div class="carousel-item"><div class="banner b2">Шинэ серум, ампул</div></div>
<div class="carousel-item"><div class="banner b3">Үнэгүй хүргэлт 100,000₮-өөс дээш</div></div></div>
<button class="carousel-control-prev" data-bs-target="#slide" data-bs-slide="prev"><span class="carousel-control-prev-icon"></span></button>
<button class="carousel-control-next" data-bs-target="#slide" data-bs-slide="next"><span class="carousel-control-next-icon"></span></button></div>
<h3 class="text-center mb-3">АНГИЛЛААР ДЭЛГҮҮР ХЭСЭХ ✨</h3><div class="row g-3 mb-5">'''+ct+'''</div>
<h3 class="text-center mb-3">BEST SELLER ✨</h3><div class="row g-3 mb-3">'''+best+'''</div><div class="text-center"><a class="btn btn-outline-dark" href="bestseller.html">Бүгдийг үзэх</a></div>''')
# categories + products
for k,(name,items) in CATS.items():
    cards=''.join(card(k,i,n,p) for i,(n,p) in enumerate(items))
    page(f'cat-{k}.html',name,f'<h2>{name}</h2><div class="row g-3 mb-3">{cards}</div>')
    n,p=items[0]
    page(f'product-{k}.html',n,f'''<div class="row"><div class="col-md-5"><div class="ph big">{n[0]}</div></div><div class="col-md-7">
<h2>{n}</h2><p class="text-warning">★★★★☆ (24 үнэлгээ)</p><p class="price fs-3">{p:,}₮</p>
<p>Ангилал: <a href="cat-{k}.html">{name}</a>. Жинхэнэ, чанарын баталгаатай гоо сайхны бүтээгдэхүүн.</p>
<table class="table"><tr><th>Арьсны төрөл</th><td>Бүх төрөл</td></tr><tr><th>Хадгалах хугацаа</th><td>24 сар</td></tr><tr><th>Найрлага</th><td>Байгалийн гаралтай</td></tr><tr><th>Хүргэлт</th><td>1-2 хоног</td></tr></table>
<input type="number" id="qty" value="1" min="1" class="form-control w-25 mb-2">
<button class="btn btn-brand add" data-name="{n}" data-price="{p}">Сагсанд нэмэх</button></div></div>''')
# search
page('search.html','Хайлт','<h2>Хайлтын үр дүн</h2><p id="sq" class="text-muted"></p><div id="results" class="row g-3"></div>')
# info + articles
arts=[('Арьсны төрлөө хэрхэн таних вэ','Тослог, хуурай, хосолмол арьсанд тохирох арчилгаа.'),('Өдөр бүрийн арчилгааны дараалал','Цэвэрлэх, тонер, серум, чийгшүүлэх, нарнаас хамгаалах.'),('Гоо сайхны бүтээгдэхүүн хадгалах сануулга','Хадгалах хугацаа, нарнаас хамгаалах, аллергийн сэрэмжлүүлэг.')]
page('info.html','Мэдээлэл','<h2>Мэдээлэл</h2><ul class="list-group">'+''.join(f'<li class="list-group-item"><a href="article{i+1}.html">{t}</a><br><small>{d}</small></li>' for i,(t,d) in enumerate(arts))+'</ul>')
for i,(t,d) in enumerate(arts): page(f'article{i+1}.html',t,f'<article><h2>{t}</h2><p>{d}</p><p>Дэлгэрэнгүй агуулга энд бичигдэнэ.</p><a href="info.html">← Буцах</a></article>')
# auth
page('login.html','Нэвтрэх','''<div class="col-md-5 mx-auto"><h2>Нэвтрэх</h2><form id="loginForm"><input class="form-control mb-2" type="email" placeholder="Имэйл" required>
<input class="form-control mb-2" type="password" placeholder="Нууц үг" required><button class="btn btn-brand w-100">Нэвтрэх</button></form><p class="mt-2">Бүртгэлгүй юу? <a href="register.html">Бүртгүүлэх</a></p></div>''')
page('register.html','Бүртгүүлэх','''<div class="col-md-5 mx-auto"><h2>Бүртгүүлэх</h2><form id="regForm"><input class="form-control mb-2" placeholder="Нэр" required>
<input class="form-control mb-2" type="email" placeholder="Имэйл" required><input class="form-control mb-2" type="tel" placeholder="Утас" required>
<input class="form-control mb-2" type="password" placeholder="Нууц үг" minlength="6" required><button class="btn btn-brand w-100">Бүртгүүлэх</button></form></div>''')
# account pages
side='<div class="list-group mb-3"><a class="list-group-item" href="profile.html">Профайл</a><a class="list-group-item" href="account.html">Данс, төлбөр</a><a class="list-group-item" href="orders.html">Захиалгын түүх</a></div>'
page('profile.html','Профайл',f'<div class="row"><div class="col-md-3">{side}</div><div class="col-md-9"><h2>Хувийн мэдээлэл</h2><form><input class="form-control mb-2" value="Бат-Эрдэнэ"><input class="form-control mb-2" value="bat@mail.mn"><input class="form-control mb-2" value="99112233"><input class="form-control mb-2" value="Улаанбаатар, СБД"><button class="btn btn-brand">Хадгалах</button></form></div></div>')
page('account.html','Данс',f'<div class="row"><div class="col-md-3">{side}</div><div class="col-md-9"><h2>Миний данс</h2><p>Үлдэгдэл: <b>150,000₮</b></p><table class="table"><tr><th>Огноо</th><th>Гүйлгээ</th><th>Дүн</th></tr><tr><td>2026-11-10</td><td>Төлбөр</td><td>-59,000₮</td></tr><tr><td>2026-11-02</td><td>Цэнэглэлт</td><td>+200,000₮</td></tr></table></div></div>')
page('orders.html','Захиалгын түүх',f'<div class="row"><div class="col-md-3">{side}</div><div class="col-md-9"><h2>Захиалгын түүх</h2><table class="table"><tr><th>№</th><th>Огноо</th><th>Төлөв</th><th>Дүн</th></tr><tr><td>1001</td><td>2026-11-10</td><td><span class="badge bg-success">Хүргэгдсэн</span></td><td>59,000₮</td></tr><tr><td>1002</td><td>2026-11-15</td><td><span class="badge bg-warning text-dark">Замд</span></td><td>129,000₮</td></tr></table></div></div>')
# cart/checkout
page('cart.html','Сагс','<h2>Сагс</h2><div id="cartBox"></div><a class="btn btn-brand" href="checkout.html">Төлбөр төлөх</a> <button class="btn btn-outline-danger" id="clear">Сагс хоослох</button>')
page('checkout.html','Төлбөр','''<h2>Төлбөр төлөх</h2><div id="sum" class="mb-3"></div><form id="payForm" class="col-md-6"><input class="form-control mb-2" placeholder="Хүргэлтийн хаяг" required>
<select class="form-select mb-2"><option>QPay</option><option>Карт</option><option>Бэлнээр</option></select><button class="btn btn-brand">Захиалах</button></form>''')
# others
page('help.html','Тусламж','''<h2>Түгээмэл асуулт</h2><div class="accordion" id="acc">'''+''.join(f'<div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#q{i}">{q}</button></h2><div id="q{i}" class="accordion-collapse collapse" data-bs-parent="#acc"><div class="accordion-body">{a}</div></div></div>' for i,(q,a) in enumerate([('Захиалга хэрхэн хийх вэ?','Бүтээгдэхүүнээ сагсанд нэмээд төлбөр төлнө.'),('Хүргэлт хэд хоног вэ?','1-2 ажлын өдөр.'),('7 хоногийн дотор.','7 хоногийн дотор.')]))+'</div>')
page('about.html','Бидний тухай','<h2>Бидний тухай</h2><p>Гоо Зүйл нь хүнс, электроник, хувцас зэрэг олон төрлийн бараа санал болгодог цахим дэлгүүр юм.</p>')
page('contact.html','Холбоо барих','<h2>Холбоо барих</h2><form class="col-md-6"><input class="form-control mb-2" placeholder="Нэр"><input class="form-control mb-2" placeholder="Имэйл"><textarea class="form-control mb-2" rows="4" placeholder="Зурвас"></textarea><button class="btn btn-brand">Илгээх</button></form>')
ALLP=[(k,n,p) for k,v in CATS.items() for n,p in v[1]]
def grid(items): return '<div class="row g-3">'+''.join(card(k,0,n,p) for k,n,p in items)+'</div>'
page('bestseller.html','Best Seller','<h2>BEST SELLER ✨</h2>'+grid(ALLP[::3]))
page('cheap.html','50,000₮-с доош','<h2>50,000₮-с доош</h2>'+grid([x for x in ALLP if x[2]<50000]))
page('sale.html','Sale %','<h2>Sale %</h2><p class="text-muted">Хямдралтай бүтээгдэхүүн</p>'+grid(ALLP[1::4]))
page('location.html','Хаяг байршил','<h2>Хаяг байршил</h2><p>Сүхбаатар дүүрэг, 1-р хороо, Улаанбаатар.</p><p>Ажлын цаг: Да-Ба 10:00-20:00</p>')
page('return.html','Буцаалтын журам','<h2>Буцаалтын журам</h2><p>Нээгээгүй, лац бүрэн бүтээгдэхүүнийг 7 хоногийн дотор буцаана.</p>')
page('policy.html','Нууцлалын бодлого','<h2>Нууцлалын бодлого</h2><p>Хэрэглэгчийн мэдээллийг гуравдагч этгээдэд дамжуулахгүй.</p>')
page('terms.html','Үйлчилгээний нөхцөл','<h2>Үйлчилгээний нөхцөл</h2><p>Сайтыг ашигласнаар үйлчилгээний нөхцөлийг зөвшөөрсөнд тооцно.</p>')
page('survey.html','Хэрэглэгчийн судалгаа','<h2>Хэрэглэгчийн судалгаа</h2><form class="col-md-6"><label>Таны арьсны төрөл</label><select class="form-select mb-2"><option>Тослог</option><option>Хуурай</option><option>Хосолмол</option><option>Мэдрэг</option></select><textarea class="form-control mb-2" placeholder="Санал"></textarea><button class="btn btn-brand">Илгээх</button></form>')
open('css/style.css','w',encoding='utf-8').write('''.logo{font-weight:800;letter-spacing:2px;color:#000;text-decoration:none;font-size:1.4rem}.subnav{background:#fff;border-top:1px solid #eee;padding:8px 0}.subnav a{margin-right:20px;color:#222;text-decoration:none;font-size:.95rem}.subnav a:hover{color:#8e3b5a}footer a{color:#ddd;text-decoration:none}.bg-brand{background:#8e3b5a}.btn-brand{background:#8e3b5a;color:#fff}.btn-brand:hover{background:#6f2c46;color:#fff}
.banner{height:260px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:2rem;font-weight:700;border-radius:8px}
.b1{background:#8e3b5a}.b2{background:#4a2c5a}.b3{background:#b5654a}
.catbox{display:block;padding:24px;text-align:center;background:#f8edf2;border-radius:8px;text-decoration:none;color:#8e3b5a;font-weight:600}
.catbox:hover{background:#efd3df}.ph{height:150px;background:#f3dde6;display:flex;align-items:center;justify-content:center;font-size:3rem;color:#8e3b5a}
.ph.big{height:320px;font-size:6rem;border-radius:8px}.price{color:#c0392b;font-weight:700}.product:hover{box-shadow:0 4px 12px rgba(0,0,0,.15)}''')
import json
PJ='const PRODUCTS='+json.dumps([{'k':k,'n':n,'p':p} for k,v in CATS.items() for n,p in v[1]],ensure_ascii=False)+';\n'
open('js/main.js','w',encoding='utf-8').write(PJ+'''const get=()=>JSON.parse(localStorage.getItem('cart')||'[]');
const save=c=>{localStorage.setItem('cart',JSON.stringify(c));count()};
function count(){const e=document.getElementById('cartCount');if(e)e.textContent=get().reduce((s,i)=>s+i.qty,0)}
document.addEventListener('click',e=>{const b=e.target.closest('.add');if(!b)return;
 const q=document.getElementById('qty'),n=q?+q.value:1,c=get(),f=c.find(i=>i.name===b.dataset.name);
 f?f.qty+=n:c.push({name:b.dataset.name,price:+b.dataset.price,qty:n});save(c);alert('Сагсанд нэмэгдлээ')});
function render(){const box=document.getElementById('cartBox');if(!box)return;const c=get();
 if(!c.length){box.innerHTML='<p>Сагс хоосон байна.</p>';return}
 box.innerHTML='<table class="table"><tr><th>Бараа</th><th>Тоо</th><th>Үнэ</th><th></th></tr>'+c.map((i,x)=>`<tr><td>${i.name}</td><td>${i.qty}</td><td>${(i.price*i.qty).toLocaleString()}₮</td><td><button class="btn btn-sm btn-danger" onclick="rm(${x})">X</button></td></tr>`).join('')+`</table><h5>Нийт: ${c.reduce((s,i)=>s+i.price*i.qty,0).toLocaleString()}₮</h5>`}
function rm(x){const c=get();c.splice(x,1);save(c);render()}
document.getElementById('clear')?.addEventListener('click',()=>{save([]);render()});
const sum=document.getElementById('sum');if(sum)sum.innerHTML='Нийт дүн: <b>'+get().reduce((s,i)=>s+i.price*i.qty,0).toLocaleString()+'₮</b>';
document.getElementById('payForm')?.addEventListener('submit',e=>{e.preventDefault();save([]);alert('Захиалга амжилттай!');location.href='orders.html'});
document.getElementById('loginForm')?.addEventListener('submit',e=>{e.preventDefault();location.href='profile.html'});
document.getElementById('regForm')?.addEventListener('submit',e=>{e.preventDefault();alert('Бүртгэгдлээ');location.href='login.html'});
const res=document.getElementById('results');
if(res){const q=(new URLSearchParams(location.search).get('q')||'').toLowerCase();document.getElementById('sq').textContent='Хайсан үг: '+q;
 const r=PRODUCTS.filter(p=>p.n.toLowerCase().includes(q));
 res.innerHTML=r.length?r.map(p=>`<div class="col-6 col-md-3"><div class="card h-100"><div class="card-body"><h6><a href="product-${p.k}.html">${p.n}</a></h6><p class="price">${p.p.toLocaleString()}₮</p><button class="btn btn-sm btn-brand add" data-name="${p.n}" data-price="${p.p}">Сагсанд нэмэх</button></div></div></div>`).join(''):'<p>Илэрц олдсонгүй.</p>'}
document.getElementById('subForm')?.addEventListener('submit',e=>{e.preventDefault();alert('Бүртгэгдлээ');e.target.reset()});\ncount();render();''')
