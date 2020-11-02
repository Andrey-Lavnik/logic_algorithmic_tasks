const sum = 1000
let a = 1
let b
let c

for(a;a<=sum/3;a++)
{
for(b = a+1;b <=sum/2;b++)
{
    c = sum - a - b
    if(a**2 + b**2 == c**2){
        console.log(a,b,c)
    }
}    
}

