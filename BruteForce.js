function bruteForce(p,s){
    ls = s.length
    lp = p.length
    max = (ls - lp +1)

    for(let i = 0; i < max ; i++){
        let flag = true
        for(let j = 0; j < lp && flag == true; j++ ){
            if(p[j] != s[j+i-1]){
                flag = false
            }
        }if(flag == true){
            return i
        }
    }
    return 0
}

let p = "as"
let s = "hola mucho gusto"

console.log(bruteForce(p,s));