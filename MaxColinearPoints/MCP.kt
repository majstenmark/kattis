

data class Point(val x: Int, val y: Int)
data class Eq(val a: Int, val b: Int, val c: Int)

fun gcd(a: Int, b:Int): Int{
  if (b == 0){
    return a
  }
  if (a == 0 || a % b == 0){
    return b
  }
  return gcd(b, a % b)

}


fun line(p1: Point, p2: Point):Eq{
  val A = (p1.y - p2.y)
  val B = (p2.x - p1.x)
  val C = (p1.x * p2.y - p2.x * p1.y)
  return Eq(A, B, -C)
}

fun lineeq(p1: Point, p2: Point): Eq{
  val eq = line(p1, p2)
  val g = gcd(gcd(eq.a, eq.b), eq.c)
  val A = eq.a / g
  val B = eq.b / g
  val C = eq.c /g

  if ((A < 0) || (A == 0 && B < 0) || (A == 0 && B == 0 && C < 0)){
    return Eq(-A, -B, -C)
  }
  return Eq(A, B, C)

}


fun main(args : Array<String>) {

  var N  = readLine()!!.toInt()
  while(N != 0){
    val points = Array<Point>(N, {Point(0, 0)})
    val eqs = HashMap<Eq, Int>()
    for (n in 0..N-1){
        val (x, y)  = readLine()!!.split(' ').map{i -> i.toInt()}
        points[n] = Point(x, y)
    }
    for (i in 0..N-2){
      for(j in i+1..N-1){
        val eq = lineeq(points[i], points[j])
        if (!eqs.contains(eq)){
          eqs.put(eq, 0)
        }
        eqs[eq] = eqs[eq]!! + 2
      }
    }
      var maxCol  = 1
      if (N == 1){
        println(1)
      }else{
          for (eq in eqs.keys){
            maxCol = Math.max(maxCol, eqs[eq]!!)
          }
          val mc = Math.sqrt(1.0 * maxCol).toInt() + 1
          println(mc)
      }
      N  = readLine()!!.toInt()
    }

}
