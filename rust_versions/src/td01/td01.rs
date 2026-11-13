const NB_ITERATIONS: i32 = 20;

fn f_activation(x: f64) -> i32 {
    return if x > 0.0 { 1 } else { 0 };
}

fn activate(tests: [(i32, i32, i32 ,i32);4]){
    let eta:f64 = 0.2;
    let mut weights: [f64; 3] = [rand::random(), rand::random(), rand::random()];
    let mut ne:i32 = 1;
    let mut iterations: i32 = 0;

    while ne != 0 && iterations < NB_ITERATIONS {
        ne = 0;
        for i in 0..tests.len(){
            let x = [tests[i].0, tests[i].1, tests[i].2];
            let d: i32 = tests[i].3;
            let S: i32 = f_activation(x[0] as f64 * weights[0] + x[1] as f64 * weights[1] + x[2] as f64 * weights[2]);
            let e = d - S;
            if e!=0 {
                ne += 1;
                for i in 0..weights.len(){
                    weights[i] = weights[i] + eta * e as f64 * x[i] as f64;
                }
            }
        }
        iterations+=1;
        println!("ne = {ne}");
    }
}

pub fn launch(){
    const OU:[(i32,i32,i32,i32);4] = [
        (0,0,1,0),
        (0,1,1,1),
        (1,0,1,1),
        (1,1,1,1)
    ];

    const ET:[(i32,i32,i32,i32);4] = [
        (0,0,1,0),
        (0,1,1,0),
        (1,0,1,0),
        (1,1,1,1),
    ];

    println!("-------------- Démarrage du OU --------------");
    activate(OU);
    println!("-------------- Démarrage du ET --------------");
    activate(ET);
}