
public class Main {

	public static void main(String[] args) {
		compression("aabcccccaaa");

	}
	
	public static String compression(String input) {
		
		char temp = input.charAt(0);
		int characterIncrement = 0;
		String result = "";
		
		for (int i = 0; i < input.length(); i++) {
			if (input.charAt(i) == temp) {
				characterIncrement++;
				System.out.println(temp);
			}
			else if (input.charAt(i) != temp) {
				result = result + ("" + temp + characterIncrement);
				temp = input.charAt(i);
				characterIncrement = 1;
			}
		}
		
		System.out.println(result);
		
		return result;
	}

}
