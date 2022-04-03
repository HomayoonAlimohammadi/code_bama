from random import sample


tags = [
'ماشین_لرنینگ',
'پایتون',
'برنامه_نویسی',
'هوش_مصنوعی',
'یادگیری_ماشین',
'یادگیری_عمیق',
'هوش_مصنوعی',
'هوشمصنوعی',
'هوشمصنوعی_آموزش',
'پایتون_مقدماتی',
'جاوا',
'برنامه_نویس',
'دیتاساینس',
'دیتاساینتیست',
'پایتون_نویسی',
'سماتک',
'علم_داده',
'داده_كاوی',
'داده',
'python',
'data_science',
'machine_learning',
'deep_learning',
'artificial_intelligence',
'ai',
'ml',
'data',
'pythonprogramming',
'machinelearning',
'datascience'
]

tags_final = ['#'+tag for tag in sample(tags, 15)]

with open('hashtags.txt', 'w') as f:
    f.write(' '.join(tags_final))