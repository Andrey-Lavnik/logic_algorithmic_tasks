let mas = [1, 2]
let x = 2
let i = 1


for(i;i<=4e6;i++)
{
    mas.push(mas[0]+mas[1])
    
    if(mas[2]%2 == 0){
        x = x+mas[2]
    }
    mas.shift()
}
console.log(x)