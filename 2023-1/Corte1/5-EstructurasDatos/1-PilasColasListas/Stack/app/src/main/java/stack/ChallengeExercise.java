package stack;

import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.Stack;
public class ChallengeExercise
{
    public boolean solve(String chain)
    {
        ArrayList<Character> input = new ArrayList<>();
        ArrayList<Character> output = new ArrayList<>();

        input.add('{');
        input.add('(');
        input.add('[');
        input.add('<');

        output.add('}');
        output.add(')');
        output.add(']');
        output.add('>');

        Stack<Character> objStack = new Stack<Character>();
        try {
            for (int i = 0; i<chain.length(); i++)
            {
                char e = chain.charAt(i);
                if (input.contains(e)){
                    objStack.push(e);
                }

                if (output.contains(e))
                {

                    char elem = objStack.pop();
                    int pos = output.indexOf(e);

                    char open = input.get(pos);

                    if (e != open)
                    {
                        return false;
                    }
                }

            }
        }
        catch (EmptyStackException e)
        {
            return false;
        }
        return objStack.empty();
    }
}
