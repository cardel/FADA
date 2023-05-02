
import java.util.HashSet;

public class Set {
	public static void main(String arg[]) {
		HashSet<Integer> objSet = new HashSet();
		objSet.add(10);
		objSet.add(20);
		objSet.add(30);
		objSet.add(10);

		for (int ai : objSet) {
			System.out.println(ai);
		}
	
	}
}
