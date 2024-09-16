var biblioteca = {
    livro : {
    autor: ['Bill Gates','Steve Jobs','Suzanne Collins'],
    título: ['The Road Ahead','Walter Isaacson','A Esperança: O Livro Final de Jogos Vorazes'],
    readingStatus: [true,true,true]
    }
    }
    console.log("------------------ STATUS ------------------ ")
    for (contador = 0 ; contador < 3 ; contador++) {
        console.log("Autor: "+ biblioteca.livro.autor[contador] + ", Título: " + biblioteca.livro.título[contador] + ", Esta sendo lido? " + biblioteca.livro.readingStatus[contador]);
        console.log(" ")
    }
    