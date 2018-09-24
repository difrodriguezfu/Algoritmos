#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>

// Compilar en https://wandbox.org, se necesita Boost

using namespace boost::multiprecision;

template<class T>
T fibonacci( T value ){
    T a = 0,b = 1, c;
    for( T i = 1; i < value; ++i ){
        c = a + b;
        a = b;
        b = c;
    }
    return c;
}

int main(){
    std::cout << "char(11): \t\t"           <<  (long)fibonacci(static_cast<char>(11)) << std::endl;             // 8 bits
    std::cout << "unsigned char(13): \t"    <<  (long)fibonacci(static_cast<unsigned char>(13)) << std::endl;   // 8 bits
    std::cout << "short(23): \t\t"          <<        fibonacci(static_cast<short>(23)) << std::endl;           // 16 bits
    std::cout << "unsigned short(24): \t"   <<        fibonacci(static_cast<unsigned short>(24)) << std::endl;  // 16 bits
    std::cout << "int(46): \t\t"            <<        fibonacci(46) << std::endl;                               // 32 bits
    std::cout << "unsigned int(47): \t"     <<        fibonacci(47u) << std::endl;                              // 32 bits
    std::cout << "long(92): \t\t"           <<        fibonacci(92ll) << std::endl;                             // 64 bits
    std::cout << "unsigned long(93): \t"    <<        fibonacci(93ull) << std::endl;                            // 64 bits
    std::cout << "boost cpp_int(1000): \t"  <<        fibonacci(cpp_int(1000)) << std::endl;                      
}