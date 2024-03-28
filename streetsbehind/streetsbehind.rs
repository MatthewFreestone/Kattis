use std::collections;
use std::io;
use std::cmp;

fn solve(n: i64, k: i64, a:i64, b:i64) -> i64 {
    let d = b-a;
    let mut k = k;
    let mut n = n;
    let mut y = d * n / a;
    if y == 0 {
        return -1;
    }
    let mut days = 0;

    while k > 0 {
        y = d * n / a;
        let x = {
            let foo = (a * (y+1)) as f64;
            (foo / d as f64).ceil() as i64
        };
        let dist_to_x = x-n;
        let steps = {
            let num = cmp::min(dist_to_x, k) as f64;
            (num / y as f64).ceil() as i64
        };
        days += steps;
        let change = steps*y;
        n += change;
        k -= change;
    }
    days
}


fn main() -> io::Result<()> {
    let mut memo = collections::HashMap::new();
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    buffer.pop();
    let t: i64 = buffer.parse().unwrap();
    for _ in 0..t {
        let mut buffer = String::new();
        io::stdin().read_line(&mut buffer)?;
        buffer.pop();
        let mut instructions = buffer.split(' ').map(|x| x.parse::<i64>().unwrap());
        let n = instructions.next().unwrap();
        let k = instructions.next().unwrap();
        let a = instructions.next().unwrap();
        let b = instructions.next().unwrap();
        let tuple = (n,k,a,b);
        match memo.get(&tuple) {
            Some(d) => println!("{d}"),
            None => {
                let d = solve(n,k,a,b);
                memo.insert(tuple, d);
                println!("{d}");
            }
        }
    }
    Ok(())
}
