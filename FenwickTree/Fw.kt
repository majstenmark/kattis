class Fenwick(N:Int){
  val arr = IntArray(N + 1)

  fun inc(i: Int, v: Int){
    private_inc(i + 1, v)
  }

  fun private_inc(ii: Int, v: Int){
    var i = ii
      while (i < arr.size){
        arr[i] += v
        i += i and -i
      }
  }
  fun sum(a: Int) = private_sum(a)


  fun private_sum(ii: Int): Int{
      var s = 0
      var i = ii
      while (i > 0){
        s += arr[i]
        i -= i and -i
      }
      return s
  }
}

/*

N, Q  = map(int, raw_input().split())
fen = FenwickTree(N)
for q in range(Q):
    query = raw_input().split()
    x = int(query[1])
    if query[0] == '+':
        y = int(query[2])
        fen.inc(x, y)
    else:
        print(fen.sum(x))
*/

fun main(args : Array<String>) {

  val (N, Q)  = readLine()!!.split(' ').map{x -> x.toInt()}

  val f = Fenwick(N)
  for (q in 1..Q){
    val query = readLine()!!.split(' ')
    val x = query[1].toInt()
    if (query[0] == "+"){
      val y = query[2].toInt()
      f.inc(x, y)
    }else{
      println(f.sum(x))
    }
  }
}
