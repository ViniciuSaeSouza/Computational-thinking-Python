public class larissa {

public static boolean checaPalindromo(String algumaString){
    int left = 0;
    int right = algumaString.length() - 1;
    while(left < right){
    if (algumaString.charAt(left) != algumaString.charAt(right)){
        return false;
    }
        left++;
        right--;
    }
    return true;
}
public static void main(String[] args) {
    System.out.println(checaPalindromo("reviver"));
}
}

