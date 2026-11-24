const PRODUCTS=[{"k": "toner", "n": "Хөвөн тонер 200мл", "p": 32000}, {"k": "toner", "n": "AHA/BHA тонер", "p": 38000}, {"k": "toner", "n": "Чийгшүүлэх тонер", "p": 29000}, {"k": "toner", "n": "Тонер жийргэвч 60ш", "p": 45000}, {"k": "serum", "n": "Серум C витамин", "p": 65000}, {"k": "serum", "n": "Ампул гиалурон", "p": 58000}, {"k": "serum", "n": "Ретинол серум", "p": 72000}, {"k": "serum", "n": "Ниацинамид ампул", "p": 49000}, {"k": "cream", "n": "Чийгшүүлэгч тос 50мл", "p": 38000}, {"k": "cream", "n": "Нүдний тос", "p": 42000}, {"k": "cream", "n": "Шөнийн тос", "p": 55000}, {"k": "cream", "n": "Нарнаас хамгаалах тос SPF50", "p": 34000}, {"k": "mask", "n": "Нүүрний хавтан маск 10ш", "p": 25000}, {"k": "mask", "n": "Шавар маск", "p": 31000}, {"k": "mask", "n": "Шөнийн маск", "p": 36000}, {"k": "mask", "n": "Уруулын маск", "p": 18000}, {"k": "makeup", "n": "Тональ тос", "p": 48000}, {"k": "makeup", "n": "Уруулын будаг", "p": 28000}, {"k": "makeup", "n": "Сормуусны гоёл", "p": 25000}, {"k": "makeup", "n": "Нүдний сүүдэр палитр", "p": 56000}, {"k": "device", "n": "Нүүр массажны багаж", "p": 78000}, {"k": "device", "n": "LED маск төхөөрөмж", "p": 320000}, {"k": "device", "n": "Ультрадуун цэвэрлэгч", "p": 95000}, {"k": "device", "n": "Гэрэлтэй толь", "p": 64000}, {"k": "hairbody", "n": "Шампунь 400мл", "p": 18000}, {"k": "hairbody", "n": "Үсний маск", "p": 32000}, {"k": "hairbody", "n": "Биеийн лосьон", "p": 26000}, {"k": "hairbody", "n": "Шүршүүрийн гель", "p": 14000}, {"k": "sun", "n": "Sun cream SPF50+", "p": 34000}, {"k": "sun", "n": "Sun stick", "p": 29000}, {"k": "sun", "n": "Sun cushion", "p": 42000}, {"k": "sun", "n": "Нарны дараах гель", "p": 22000}];
const get=()=>JSON.parse(localStorage.getItem('cart')||'[]');
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
const USERS_KEY='kgUsers';
const CURRENT_KEY='kgCurrentUser';
const readUsers=()=>JSON.parse(localStorage.getItem(USERS_KEY)||'{}');
const setMessage=(id,message,ok=false)=>{const e=document.getElementById(id);if(e){e.textContent=message;e.className='small mb-2 '+(ok?'text-success':'text-danger')}};
async function passwordHash(password,salt){
 if(!globalThis.crypto?.subtle) throw new Error('Аюулгүй нууц үгийн шалгалт боломжгүй байна. Сайтаа localhost дээр нээнэ үү.');
 const bytes=new TextEncoder().encode(salt+password); const hash=await crypto.subtle.digest('SHA-256',bytes);
 return Array.from(new Uint8Array(hash),b=>b.toString(16).padStart(2,'0')).join('');
}
document.getElementById('regForm')?.addEventListener('submit',async e=>{
 e.preventDefault(); const email=document.getElementById('regEmail').value.trim().toLowerCase();
 try {const users=readUsers(); if(users[email]){setMessage('regMessage','Энэ имэйлээр бүртгэл үүссэн байна. Нэвтэрнэ үү.');return;}
 const salt=Array.from(crypto.getRandomValues(new Uint8Array(16)),b=>b.toString(16).padStart(2,'0')).join('');
 users[email]={name:document.getElementById('regName').value.trim(),email,phone:document.getElementById('regPhone').value.trim(),address:'',salt,passwordHash:await passwordHash(document.getElementById('regPassword').value,salt)};
 localStorage.setItem(USERS_KEY,JSON.stringify(users)); location.href='login.html?email='+encodeURIComponent(email);
 } catch(err){setMessage('regMessage',err.message||'Бүртгэл хадгалахад алдаа гарлаа.');}
});
document.getElementById('loginForm')?.addEventListener('submit',async e=>{
 e.preventDefault(); const email=document.getElementById('loginEmail').value.trim().toLowerCase(), password=document.getElementById('loginPassword').value;
 try {const user=readUsers()[email]; if(!user||await passwordHash(password,user.salt)!==user.passwordHash){setMessage('loginMessage','Имэйл эсвэл нууц үг буруу байна.');return;}
 localStorage.setItem(CURRENT_KEY,email); location.href='profile.html';
 } catch(err){setMessage('loginMessage',err.message||'Нэвтрэх үед алдаа гарлаа.');}
});
const loginEmailField=document.getElementById('loginEmail'); if(loginEmailField){loginEmailField.value=new URLSearchParams(location.search).get('email')||'';}
const profileForm=document.getElementById('profileForm');
if(profileForm){
 const email=localStorage.getItem(CURRENT_KEY), user=readUsers()[email];
 if(!user){location.href='login.html';}
 else {document.getElementById('profileName').value=user.name||'';document.getElementById('profileEmail').value=user.email||'';document.getElementById('profilePhone').value=user.phone||'';document.getElementById('profileAddress').value=user.address||'';}
 profileForm.addEventListener('submit',e=>{e.preventDefault();const users=readUsers(),oldEmail=localStorage.getItem(CURRENT_KEY),old=users[oldEmail];if(!old)return;
 const email=document.getElementById('profileEmail').value.trim().toLowerCase();if(email!==oldEmail&&users[email]){setMessage('profileMessage','Энэ имэйл өөр хэрэглэгчид бүртгэлтэй байна.');return;}
 old.name=document.getElementById('profileName').value.trim();old.phone=document.getElementById('profilePhone').value.trim();old.address=document.getElementById('profileAddress').value.trim();old.email=email;
 if(email!==oldEmail){delete users[oldEmail];users[email]=old;localStorage.setItem(CURRENT_KEY,email);}localStorage.setItem(USERS_KEY,JSON.stringify(users));setMessage('profileMessage','Мэдээлэл амжилттай хадгалагдлаа.',true);
 });
 document.getElementById('logoutButton')?.addEventListener('click',()=>{localStorage.removeItem(CURRENT_KEY);location.href='login.html';});
}
const PRODUCT_IMAGES={toner:'toner',serum:'serum',cream:'cream',mask:'mask',makeup:'makeup',device:'device',hairbody:'hairbody',sun:'sun'};
function productCategory(name){return /нарнаас|sun|SPF/i.test(name)?'sun':PRODUCTS.find(p=>p.n===name)?.k||(/toner/i.test(name)?'toner':/serum|ампул|ретинол|ниацинамид/i.test(name)?'serum':/тос|cream/i.test(name)?'cream':/маск/i.test(name)?'mask':/шампунь|үс|бие|гель/i.test(name)?'hairbody':/төхөөрөмж|LED|багаж|цэвэрлэгч|толь/i.test(name)?'device':/будаг|сормуус|makeup|тональ|палитр/i.test(name)?'makeup':'serum');}
function productImagePath(name){return 'images/products/'+(PRODUCT_IMAGES[productCategory(name)]||'serum')+'.jpg';}
function attachProductPhotos(){document.querySelectorAll('.ph').forEach(box=>{const card=box.closest('.product');const button=(card||document.querySelector('main'))?.querySelector('.add');const name=button?.dataset.name||document.querySelector('main h2')?.textContent?.trim()||'Гоо сайхны бүтээгдэхүүн';const img=document.createElement('img');img.className='product-photo';img.src=productImagePath(name);img.alt=name;img.loading='lazy';img.decoding='async';box.replaceChildren(img);});}
const res=document.getElementById('results');
if(res){const q=(new URLSearchParams(location.search).get('q')||'').toLowerCase();document.getElementById('sq').textContent='Хайсан үг: '+q;
 const r=PRODUCTS.filter(p=>p.n.toLowerCase().includes(q));
 res.innerHTML=r.length?r.map(p=>`<div class="col-6 col-md-3"><div class="card h-100 product"><div class="ph"><img class="product-photo" src="${productImagePath(p.n)}" alt="${p.n}" loading="lazy" decoding="async"></div><div class="card-body"><h6><a href="product-${p.k}.html">${p.n}</a></h6><p class="price">${p.p.toLocaleString()}₮</p><button class="btn btn-sm btn-brand add" data-name="${p.n}" data-price="${p.p}">Сагсанд нэмэх</button></div></div></div>`).join(''):'<p>Илэрц олдсонгүй.</p>'}
document.getElementById('subForm')?.addEventListener('submit',e=>{e.preventDefault();alert('Бүртгэгдлээ');e.target.reset()});
count();render();attachProductPhotos();


