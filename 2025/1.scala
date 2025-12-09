import scala.io.Source

def convert(x: String) = x match {
  case s"L$turn" => -turn.toInt
  case s"R$turn" => turn.toInt
}

def solve1(lines: Iterable[String]) = lines.map(convert).foldLeft((50, 0)){
  case ((tick, count), offset) =>
    val newTick = Math.floorMod(tick+offset, 100)
    (newTick, count+(if newTick==0 then 1 else 0))
}._2

def solve2(lines: Iterable[String]) = lines.map(convert).foldLeft((50, 0)){
  case ((tick, count), offset) =>
    val newTick = Math.floorMod(tick+offset, 100)
    val divResult = Math.floorDiv(tick+offset, 100)
    val correctLeftStart0 = if divResult < 0 && tick == 0 then -1 else 0
    val correctLeftEnd0 = if divResult <= 0 && newTick == 0 then 1 else 0
    val passZero = Math.abs(divResult)+correctLeftStart0+correctLeftEnd0
    // println((tick, offset, newTick, passZero))
    (newTick, count+passZero)
}._2

@main def main() = {
  val lines = Source.stdin.getLines().toList
  println(solve1(lines))
  println(solve2(lines))
}
