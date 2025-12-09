import scala.io.Source

def findMaxSubsequence(nDigits: Int)(line: String) = {
  var startRange = 0
  val pickedChars = for i <- (nDigits-1 to 0 by -1) yield {
    val maxChar = line.view.slice(startRange, line.length-i).max;
    val idx = line.indexOf(maxChar, startRange);
    startRange = idx+1;
    maxChar
  }
  pickedChars.mkString.toLong
}

def solve1(lines: Iterable[String]) = lines.map(findMaxSubsequence(2)).sum

def solve2(lines: Iterable[String]) = lines.map(findMaxSubsequence(12)).sum

@main def main() = {
  val lines = Source.stdin.getLines().toList
  println(solve1(lines))
  println(solve2(lines))
}
