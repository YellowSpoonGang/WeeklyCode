import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		permutation("Tact Coa", "");
		ArrayList<String> finalAnswer = new ArrayList<String>();
		boolean isPalindrome = false;
		for (int i = 0; i < 500; i++) {
			if (palindrome(temp.get(i))) {
				finalAnswer.add(temp.get(i));
				isPalindrome = true;
			}
		}
		
		System.out.print(isPalindrome + " (Permutations: ");
		for (int i = 0; i < finalAnswer.size(); i++) {
			System.out.print("\"" + finalAnswer.get(i) + "\", ");
		}
		System.out.print(")");
	}
	
	public static boolean palindrome(String input) {
		
		boolean answer = false;
		input = input.toLowerCase();
		int otherEnd = input.length() - 1;
		for (int i = 0; i < input.length(); i++) {
			if (input.charAt(i) == input.charAt(otherEnd)) {
				answer = true;
				otherEnd--;
			}
			else {
				otherEnd--;
				return answer;
			}			
		}
		return answer;
	}

	int permIndex = 0;
	static ArrayList<String> temp = new ArrayList<String>();
	public static void permutation(String input, String output) {
		
		if (input.length() == 0) {
			temp.add(output);
		}
		
		for (int i = 0; i < input.length(); i++) {
			char temp = input.charAt(i);
			String previous = input.substring(0,i) + input.substring(i+1);
			permutation(previous, output + temp);
		}
		
	}
}
