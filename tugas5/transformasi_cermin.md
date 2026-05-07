# Visualisasi Transformasi Cermin terhadap Sumbu-X

Transformasi pencerminan terhadap sumbu-X menggunakan rumus:

\[
(x, y) \rightarrow (x, -y)
\]

---

<style>
canvas{
    border:2px solid black;
    margin-top:20px;
}
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>

<div id="animasi"></div>

<script>

let points = [
    [2,1],
    [3,1],
    [3,4],
    [2,4]
];

function setup(){

    let canvas = createCanvas(700,700);
    canvas.parent("animasi");

    textFont('Arial');
}

function draw(){

    background(255);

    translate(width/2,height/2);

    scale(50,-50);

    // =========================
    // GRID
    // =========================

    stroke(220);
    strokeWeight(0.02);

    for(let i=-10;i<=10;i++){

        line(i,-10,i,10);
        line(-10,i,10,i);
    }

    // =========================
    // SUMBU X Y
    // =========================

    stroke(0);
    strokeWeight(0.05);

    line(-10,0,10,0);
    line(0,-10,0,10);

    // =========================
    // GERAK
    // =========================

    let gerak = sin(frameCount * 0.03) * 1.5;

    // =========================
    // OBJEK ASLI
    // =========================

    let objek = [];

    for(let p of points){

        objek.push([
            p[0],
            p[1] + gerak
        ]);
    }

    // =========================
    // BAYANGAN CERMIN
    // =========================

    let cermin = [];

    for(let p of objek){

        cermin.push([
            p[0],
            -p[1]
        ]);
    }

    // =========================
    // GARIS CERMIN
    // =========================

    stroke('purple');
    strokeWeight(0.07);

    line(-10,0,10,0);

    // =========================
    // OBJEK ASLI
    // =========================

    fill('blue');
    stroke('blue');
    strokeWeight(0.08);

    beginShape();

    for(let p of objek){

        vertex(p[0],p[1]);
        circle(p[0],p[1],0.15);
    }

    endShape(CLOSE);

    // =========================
    // BAYANGAN
    // =========================

    fill('red');
    stroke('red');

    beginShape();

    for(let p of cermin){

        vertex(p[0],p[1]);
        circle(p[0],p[1],0.15);
    }

    endShape(CLOSE);

    // =========================
    // LABEL
    // =========================

    scale(1,-1);

    fill('blue');
    noStroke();
    textSize(0.3);

    let labels = ["G","H","C","B"];

    for(let i=0;i<objek.length;i++){

        let x = objek[i][0];
        let y = -objek[i][1];

        text(
            labels[i] + 
            " (" + 
            objek[i][0].toFixed(1) + 
            "," + 
            objek[i][1].toFixed(1) + 
            ")",
            x + 0.2,
            y - 0.2
        );
    }

    fill('red');

    for(let i=0;i<cermin.length;i++){

        let x = cermin[i][0];
        let y = -cermin[i][1];

        text(
            labels[i] + "'" +
            " (" +
            cermin[i][0].toFixed(1) +
            "," +
            cermin[i][1].toFixed(1) +
            ")",
            x + 0.2,
            y - 0.2
        );
    }
}

</script>

---

## Penjelasan

- Biru → Objek asli
- Merah → Bayangan cermin
- Ungu → Garis cermin (sumbu-X)

Rumus pencerminan:

\[
(x,y)\rightarrow(x,-y)
\]

Objek bergerak naik turun dan bayangannya mengikuti secara simetris.
