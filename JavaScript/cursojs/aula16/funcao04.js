function fatorial(n){
   var res = 1
   for(var c=n; c>0; c--){
     res *= c
   }
   return res
}
console.log(fatorial(5))