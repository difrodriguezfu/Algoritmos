import java.math.BigInteger;

public class Fibonacci{
    public static byte bit8( byte value ){
        byte a = 0,b = 1, c = 0;
        for( byte i = 1; i < value; ++i ){
            c = (byte)(a + b);
            a = b;
            b = c;
        }
        return c;
    }

    public static short bit16( short value ){
        short a = 0,b = 1, c = 0;
        for( short i = 1; i < value; ++i ){
            c = (short)(a + b);
            a = b;
            b = c;
        }
        return c;
    }

    public static int bit32( int value ){
        int a = 0,b = 1, c = 0;
        for( int i = 1; i < value; ++i ){
            c = (int)(a + b);
            a = b;
            b = c;
        }
        return c;
    }

    public static long bit32( long value ){
        long a = 0,b = 1, c = 0;
        for( long i = 1; i < value; ++i ){
            c = (long)(a + b);
            a = b;
            b = c;
        }
        return c;
    }

    public static void main(String[] args){
        System.out.println("8  Bits: " + Fibonacci.bit8((byte)11));
        System.out.println("16 Bits: " + Fibonacci.bit16((short)23));
        System.out.println("32 Bits: " + Fibonacci.bit32(46));
        System.out.println("64 Bits: " + Fibonacci.bit32((long)92));
    }
}