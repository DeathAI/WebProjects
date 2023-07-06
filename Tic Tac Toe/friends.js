let win = " "
let list = [ [1,'one'],
            [2,'two'],
            [3,'three'],

            [4,'four'],
            [5,'five'],
            [6,'six'],

            [7,'seven'],
            [8,'eight'],
            [9,'nine']
        ]
let p1Name = ''
let p2Name = ''
let history = ''
let Next = ''
let c = changes = 0
function checkif(values,a,b,c){
    if(values[a]==values[b] && values[b]==values[c] && values[a]!=' '){
        if(values[a]=="X"){
            let p1 = document.getElementById("p1Name")
            p1Name = p1.value
            win = p1Name
        }
        else{
            alert('o')
            let p2 = document.getElementById("p2Name")
            p2Name = p2.value
            win = p2Name
        }
        return true
    }
    else
        return false
}
function check(values){
    return ( checkif(values,0,1,2) || checkif(values,3,4,5) || checkif(values,6,7,8) || checkif(values,0,4,8) || checkif(values,2,4,6) || checkif(values,0,3,6) || checkif(values,1,4,7) || checkif(values,2,5,8) )
}
function iswin(){
    let local = [ 
                    '', '', '',
                    '', '', '',
                    '', '', '' 
                ]
    for(let i = 0 ; i<9 ; i++){
        let tmp = document.getElementById(list[i][1])
        let s = String(tmp.textContent)
        if(s=="" || s==undefined)
            local[i]=" "
        else
            local[i]=s
    }
    if(check(local)){
        // let dis = document.getElementById("winIndicator")
        alert(String(win)+" is won this game")
        let over = document.getElementById("over")
        for(let i=0;i<10;i++){
            over.style.display = "block"
            over.style.opacity = 0
            setTimeout(function(){
                over.style.textDecoration = "none"
            }, 3000)
            setTimeout(function(){
                over.style.textDecoration = "underline"
            }, 1000)
        }
          
    }
    else{
        if(c==9){
            let dis = document.getElementById("winIndicator")
            dis.textContent = "Draw"
            let over = document.getElementById("over")
            over.style.display = "block"
        }
    }
}
function next(){
    let tmp = String(Next).split(' ')
    if(changes>0){
        // assignning Data to add X or O on page
        let x = document.getElementById(tmp[0])
        if(c%2==0)
            x.textContent = "X"
        else
            x.textContent = "O"
        c++
        // again add value in history cause we also do back again and again
        if(c==0)
            history = tmp[0] + history
        else
            history = tmp[0] + ' ' + history
        delete tmp[0]
        let y = ""
        tmp.forEach(i => {
            if(i!=undefined){
                y = y + String(i) + " "
            }
        });
        Next = y
        changes--
        if(c>=5)
            iswin()
    }
    else{
        alert("No Changes are Posible")
    }
}
function back(){
    let tmp = String(history).split(' ')
    win = " "
    if(c>0){
        let x = document.getElementById(tmp[0])
        // assignning Data to delete X or O on page
        x.textContent = ""
        // saving another history for the next button
        if(c==0)
            Next = tmp[0] + Next
        else
            Next = tmp[0] + ' ' + Next
        changes++
        delete tmp[0]
        let y = ""
        tmp.forEach(i => {
            if(i!=undefined){
                y = y + String(i) + " "
            }
        });
        history = y
        c--
    }
    else{
        alert("Game is not started yet")
    }
}
function update(id){
    for(let i=0;i<9;i++){
        if(id === list[i][0]){
            let cur = document.getElementById(list[i][1])
            if(cur.textContent=="" && win==' '){
                if(c%2==0)
                    cur.textContent = "X"
                else
                    cur.textContent = "O"
                c++
                // saving another history for the back button
                if(c==0)
                    history = list[i][1] + history
                else
                    history = list[i][1] + ' ' + history
                if(c>=5)
                    iswin()
            }
        }
    }
}
function restart(){
    for(let i=0;i<9;i++){
        let x = document.getElementById(list[i][1])
        x.textContent = ""
    }
    win = ' '
    history = ''
    Next = ''
    c = 0
    changes = 0
    let dis = document.getElementById("winIndicator")
    dis.textContent = ""
    let over = document.getElementById("over")
    over.style.display = "none"
}

function p1Data(){
    const p1 = document.getElementById("p1Name")
    p1Name = p1.value
    alert(p1Name+"'s Data is saved")
    const file1 = new File([p1Name], "p1.txt", {type: "text/plain"})
}

function p2Data(){
    const p2 = document.getElementById("p2Name")
    p2Name = p2.value
    alert(p2Name+"'s Data is saved")
    const file2 = new File([p2Name], "p2.txt", {type: "text/plain"})
    console.log(file2);
}

function loadImg(){
    if('p1.txt' in window.FileList){
        alert()
    }
}