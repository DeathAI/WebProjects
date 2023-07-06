class Game {
    constructor() {
        this.moveOf="";
        this.Counter=0;
        this.all = {
            A1: "fa-solid fa-chess-rook-piece",
            A2: "fa-solid fa-chess-knight-piece",
            A3: "fa-solid fa-chess-bishop-piece",
            A4: "fa-solid fa-chess-queen-piece",
            A5: "fa-solid fa-chess-king-piece",
            A6: "fa-solid fa-chess-bishop-piece",
            A7: "fa-solid fa-chess-knight-piece",
            A8: "fa-solid fa-chess-rook-piece",
            
            B1: "fa-solid fa-chess-pawn-piece",
            B2: "fa-solid fa-chess-pawn-piece",
            B3: "fa-solid fa-chess-pawn-piece",
            B4: "fa-solid fa-chess-pawn-piece",
            B5: "fa-solid fa-chess-pawn-piece",
            B6: "fa-solid fa-chess-pawn-piece",
            B7: "fa-solid fa-chess-pawn-piece",
            B8: "fa-solid fa-chess-pawn-piece",
            
            C1: "",
            C2: "",
            C3: "",
            C4: "",
            C5: "",
            C6: "",
            C7: "",
            C8: "",
            
            D1: "",
            D2: "",
            D3: "",
            D4: "",
            D5: "",
            D6: "",
            D7: "",
            D8: "",
            
            E1: "",
            E2: "",
            E3: "",
            E4: "",
            E5: "",
            E6: "",
            E7: "",
            E8: "",
            
            F1: "",
            F2: "",
            F3: "",
            F4: "",
            F5: "",
            F6: "",
            F7: "",
            F8: "",

            G1: "fa-thin fa-chess-pawn-piece",
            G2: "fa-thin fa-chess-pawn-piece",
            G3: "fa-thin fa-chess-pawn-piece",
            G4: "fa-thin fa-chess-pawn-piece",
            G5: "fa-thin fa-chess-pawn-piece",
            G6: "fa-thin fa-chess-pawn-piece",
            G7: "fa-thin fa-chess-pawn-piece",
            G8: "fa-thin fa-chess-pawn-piece",

            H1: "fa-thin fa-chess-rook-piece",
            H2: "fa-thin fa-chess-knight-piece",
            H3: "fa-thin fa-chess-bishop-piece",
            H4: "fa-thin fa-chess-queen-piece",
            H5: "fa-thin fa-chess-king-piece",
            H6: "fa-thin fa-chess-bishop-piece",
            H7: "fa-thin fa-chess-knight-piece",
            H8: "fa-thin fa-chess-rook-piece",
        }; // assign classes to display cokies of chess
        for (let key in this.all) {
            if(key === "")
                continue

            let element = document.getElementById(key);
            let classes = String(this.all[key]).split(" ");

            if(classes[0] === "")
                continue
            element.classList.add(classes[0]);

            if(classes[1] === "")
                continue
            element.classList.add(classes[1]);
        }
        // to track wich cokies are where in chess board
        this.chessboard = [
            ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook'],
            ['Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn'],
            ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook']
          ];
        // to track is this team cookies or not
        this.chessTeam = [
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
          ];
          this.player1List = [];
          this.player2List = [];
    }
    
    dispSuggestion(){
        // alert(String(this.posibleMovesList))
        console.log(String(this.chessTeam).replace("],","],\n\r"))
        console.log(String(this.chessboard).replace("],","],\n\r"))
        for(let ID in this.posibleMovesList) {
            document.getElementById(this.posibleMovesList[ID]).style.backgroundColor = "#333b";
            // document.getElementById(ID).style.border = "1px solid green";
        }
    }
    eraseSuggetion(){
        for(let key in this.all) {
            document.getElementById(key).style.backgroundColor = "#3330";
            // document.getElementById(ID).style.border = "1px solid green";
        }
    }
    suggestedMove(moveID){
        let char = moveID[0];
        let i1=char.charCodeAt()-65;
        char = moveID[1];
        let i2=char.charCodeAt()-49;
        let Name = this.chessboard[i1][i2];
        var i__1=i1;
        var i__2=i2;
        this.posibleMovesList = [];
        switch(Name){
            case 'Rook': 
                    i__1=i1;
                    i__2=i2;
                    while(i__1<8){
                        i__1++;
                        if(i__1==8)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 1.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 1 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__1>=0){
                        i__1--;
                        if(i__1==-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 2.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 2 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__2>=0){
                        i__2--;
                        if(i__2==-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 3.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 3 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__2<8){
                        i__2++;
                        if(i__2==8)
                            break
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 4.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 4 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }
                    this.dispSuggestion()
                    break;
            case 'Bishop': 
                    i__1=i1;
                    i__2=i2;
                    while(i__1<8 && i__2<8){
                        i__1++;
                        i__2++;
                        if(i__1>=8 || i__1<=-1)
                            break;
                        if(i__2>=8 || i__2<=-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 1.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 1 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__1>=0 && i__2<8){
                        i__1--;
                        i__2++;
                        if(i__1>=8 || i__1<=-1)
                            break;
                        if(i__2>=8 || i__2<=-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 2.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 2 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__2>=0 && i__1>=0){
                        i__1--;
                        i__2--;
                        if(i__1>=8 || i__1<=-1)
                            break;
                        if(i__2>=8 || i__2<=-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 3.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 3 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__1<8 && i__2>=0){
                        i__1++;
                        i__2--;
                        if(i__1>=8 || i__1<=-1)
                            break;
                        if(i__2>=8 || i__2<=-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 4.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 4 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }
                    this.dispSuggestion();
                    break;
            case 'Knight':
                    var j1 = i1 + 2;
                    var j2 = i2 + 1;
                    if(j1<8){
                        if(j2<8 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2]){
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        }
                        j2-=2;
                        if(j2>=0 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2]){
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        }
                    }

                    var j1 = i1 - 2;
                    var j2 = i2 + 1;
                    if(j1>=0){
                        if(j2<8 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2]){
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        }
                        j2-=2;
                        if(j2>=0 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2]){
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        }
                    }

                    var j1 = i1 + 1;
                    var j2 = i2 + 2;
                    if(j2<8){
                        if(j1<8 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2]){
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        }
                        j1-=2;
                        if(j1>=0 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2]){
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        }
                    }

                    var j1 = i1 + 1;
                    var j2 = i2 - 2;
                    if(j2>=0){
                        if(j1<8 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2]){
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        }
                        j1-=2;
                        if(j1>=0 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2]){
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        }
                    }
                    this.dispSuggestion();
                    break;
            case 'Queen': 
                    i__1=i1;
                    i__2=i2;
                    while(i__1<8){
                        i__1++;
                        if(i__1==8)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 1.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 1 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__1>=0){
                        i__1--;
                        if(i__1==-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 2.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 2 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__2>=0){
                        i__2--;
                        if(i__2==-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 3.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 3 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__2<8){
                        i__2++;
                        if(i__2==8)
                            break
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 4.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 4 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }
                    i__1=i1;
                    i__2=i2;
                    while(i__1<8 && i__2<8){
                        i__1++;
                        i__2++;
                        if(i__1>=8 || i__1<=-1)
                            break;
                        if(i__2>=8 || i__2<=-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 1.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 1 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__1>=0 && i__2<8){
                        i__1--;
                        i__2++;
                        if(i__1>=8 || i__1<=-1)
                            break;
                        if(i__2>=8 || i__2<=-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 2.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 2 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__2>=0 && i__1>=0){
                        i__1--;
                        i__2--;
                        if(i__1>=8 || i__1<=-1)
                            break;
                        if(i__2>=8 || i__2<=-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 3.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 3 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }

                    i__1=i1;
                    i__2=i2;
                    while(i__1<8 && i__2>=0){
                        i__1++;
                        i__2--;
                        if(i__1>=8 || i__1<=-1)
                            break;
                        if(i__2>=8 || i__2<=-1)
                            break;
                        if(this.chessTeam[i__1][i__2] !== ''){
                            if(this.chessTeam[i__1][i__2] !== this.chessTeam[i1][i2]){
                                // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 4.1 ==>");
                                this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                            }
                            break;
                        }
                        // alert(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49)+"<== 4 ==>");
                        this.posibleMovesList.push(String.fromCharCode(i__1+65)+String.fromCharCode(i__2+49));
                    }
                    this.dispSuggestion()
                    break;
            case 'King':
                    var j1 = i1;
                    var j2 = i2+1;
                    if(j2<8 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2])
                        this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                    j2-=2;
                    if(j2>=0 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2])
                        this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));

                    var j1 = i1+1;
                    var j2 = i2;
                    if(j1<8){
                        if(this.chessTeam[j1][j2] != this.chessTeam[i1][i2])
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        j2++
                        if(j2<8 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2])
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        j2-=2;
                        if(j2>=0 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2])
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                    }

                    var j1 = i1 - 1;
                    var j2 = i2;
                    if(j1>=0){
                        if(this.chessTeam[j1][j2] != this.chessTeam[i1][i2])
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        j2++
                        if(j2<8 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2]){
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        }
                        j2-=2;
                        if(j2>=0 && this.chessTeam[j1][j2] != this.chessTeam[i1][i2]){
                            this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        }
                    }
                    this.dispSuggestion();
                    break;
            case 'Pawn':
                    let element = document.getElementById(moveID);
                    var j1 = i1+1
                    var j2 = i2 
                    if (element.classList.contains("fa-solid") && i1==1 && this.chessTeam[j1][j2] === "" && this.chessTeam[j1+1][j2] === "" ) {
                        this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        this.posibleMovesList.push(String.fromCharCode(j1+66)+String.fromCharCode(j2+49));
                    } else if(element.classList.contains("fa-solid") && j1>1 && j1<8 && this.chessTeam[j1][j2] === "") {
                        this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                    }

                    j1 = i1 + 1;
                    j2 = j2 - 1;
                    if(element.classList.contains("fa-solid") && j1<8 && j2>=0  && this.chessTeam[j1][j2] !== "") {
                        this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                    }
                    j2 = j2+2;
                    if(element.classList.contains("fa-solid") && j1<8 && j2<8  && this.chessTeam[j1][j2] !== "") {
                        this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                    }

                    
                    j1 = i1-1;
                    j2 = i2;
                    if (element.classList.contains("fa-thin") && i1==6 && this.chessTeam[j1][j2] === "" && this.chessTeam[j1-1][j2] === "" ) {
                        this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                        this.posibleMovesList.push(String.fromCharCode(j1+64)+String.fromCharCode(j2+49));
                    } else if(element.classList.contains("fa-thin") && j1>1 && j1<8 && this.chessTeam[j1][j2] === "") {
                        this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                    }

                    j1 = i1-1;
                    j2 = j2-1;
                    if(element.classList.contains("fa-thin") && j1>=0 && j2>=0 && this.chessTeam[j1][j2] !== "") {
                        this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                    }
                    j2 = j2+2;
                    if(element.classList.contains("fa-thin") && j1>=0 && j2<8  && this.chessTeam[j1][j2] !== "") {
                        this.posibleMovesList.push(String.fromCharCode(j1+65)+String.fromCharCode(j2+49));
                    }

                    this.dispSuggestion();
                    break;
            case '':
            default:    
                    this.move(moveID);
                    break;
        }
    }
    Valid_Move(moveOf, moveID){
        if(this.posibleMovesList.includes(moveID)){
            let char = moveID[0];
            let i1=char.charCodeAt()-65;
            char = moveID[1];
            let i2=char.charCodeAt()-49;

            char = moveOf[0];
            let j1=char.charCodeAt()-65;
            char = moveOf[1];
            let j2=char.charCodeAt()-49;

            if(this.chessboard[i1][i2]!=""){
                if(document.getElementById(moveID).classList.contains("fa-solid")){
                    this.player1List.push(this.all[moveID]);
                }else{
                    this.player2List.push(this.all[moveID]);
                }
            }

            this.chessboard[i1][i2] = this.chessboard[j1][j2];
            this.chessboard[j1][j2] = '';

            this.chessTeam[i1][i2] = this.chessTeam[j1][j2];
            this.chessTeam[j1][j2] = '';

            if(this.all[moveID] !== ""){
                var classes = String(this.all[moveID]).split(" ")
                document.getElementById(moveID).classList.remove(classes[0]);
                document.getElementById(moveID).classList.remove(classes[1]);
            }
            var element = document.getElementById(moveOf);
            var classes = String(this.all[moveOf]).split(" ");
            element.classList.remove(classes[0]);
            element.classList.remove(classes[1]);

            this.all[moveID]=this.all[moveOf];
            this.all[moveOf]="";

            this.moveOf="";
            for (let key in this.all) {
                if(key === "")
                    continue
    
                let element = document.getElementById(key);
                let classes = String(this.all[key]).split(" ");
    
                if(classes[0] === "")
                    continue
                element.classList.add(classes[0]);
    
                if(classes[1] === "")
                    continue
                element.classList.add(classes[1]);
            }
            let king1="";
            let king2="";
            let c=0;
            for(let row in this.chessboard) {
                if(row.includes("King") && king1==="")
                    king1 = String.fromCharCode(c+65)+String.fromCharCode(row.indexOf("King")+49)
                if(row.includes("King") && king1!=="")
                    king2 = String.fromCharCode(c+65)+String.fromCharCode(row.indexOf("King")+49)
                c++;
            }
            if(king2===""){
                let player = "";
                if(document.getElementById(king1).classList.contains("fa-solid")){ player="Player 2"}else{ player="Player 2"}
                alert("Game is Over \n\r"+player+" is Won this game.")
            }
        }
        else{
            this.Counter--;
            alert("sorry invalid moves")
        }
    }
    move(moveID){
        this.eraseSuggetion();
        if(document.getElementById(moveID).classList.contains("fa-solid") && this.Counter%2==0 && this.moveOf===""){
            return;
        }else if(document.getElementById(moveID).classList.contains("fa-thin") && this.Counter%2==1 && this.moveOf===""){
            return;
        }
        // alert(this.Counter)
        if(this.moveOf!="" && this.moveOf!=undefined){
            if(this.moveOf === moveID){
                alert(moveID+' is deselected')
                document.getElementById(moveID).style.border = "none";
                this.moveOf="";
                return;
            }else{
                document.getElementById(this.moveOf).style.border = "none";
                this.Counter++;
                this.Valid_Move(this.moveOf, moveID);
                this.moveOf="";
            }
        }else{
            if(this.all[moveID]!=""){
                let char = moveID[0];
                let n1=char.charCodeAt()-65;
                char = moveID[1];
                let n2=char.charCodeAt()-49;
                if(this.chessboard[n1][n2]!=""){
                    this.moveOf = moveID;
                    // alert(moveID+' is selected');
                    this.suggestedMove(moveID);
                    document.getElementById(moveID).style.border = "1px solid red";
                }
                else
                    alert('there is nothing to move - this error may be fake');
            }
            else{
                alert('there is nothing to move');
            }
        }
    }
  }
