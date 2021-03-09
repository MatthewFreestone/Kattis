#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "Teque.cpp"
#include <vector>

TEST_CASE("Teque Basic Tests") {
	Teque t;
    REQUIRE (t.size() == 0);
    REQUIRE (t.to_vector().size() == 0);
    SECTION("Adding to front"){
    	t.push_front(1);
    	t.push_front(2);
    	t.push_front(3);
    	t.push_front(4);
    	t.push_front(5);
    	t.push_front(6);
    	t.push_front(7);
    	t.push_front(8);
    	std::vector<int> v{8,7,6,5,4,3,2,1};
    	REQUIRE (t.size() == 8);
    	REQUIRE (t.to_vector() == v);
    }
    SECTION("Adding to back"){
    	t.push_back(1);
    	t.push_back(2);
    	t.push_back(3);
    	t.push_back(4);
    	t.push_back(5);
    	t.push_back(6);
    	t.push_back(7);
    	t.push_back(8);
    	std::vector<int> v{1,2,3,4,5,6,7,8};
    	REQUIRE (t.size() == 8);
    	REQUIRE (t.to_vector() == v);
    }
    SECTION("Adding to middle"){
    	t.push_middle(1);
    	t.push_middle(2);
    	t.push_middle(3);
    	t.push_middle(4);
    	t.push_middle(5);
    	t.push_middle(6);
    	t.push_middle(7);
    	std::vector<int> v{1,3,5,7,6,4,2};
    	REQUIRE (t.size() == 7);
    	REQUIRE (t.to_vector() == v);
    }
    SECTION("Kattis first test"){
    	t.push_back(9);
    	t.push_front(3);
    	t.push_middle(5);
    	REQUIRE (t.get(0) == 3);
    	REQUIRE (t.get(1) == 5);
    	REQUIRE (t.get(2) == 9);

    	//Added Tests
    	std::vector<int> v{3,5,9};
    	REQUIRE (t.size() == 3);
    	REQUIRE (t.to_vector() == v);
    	

    	SECTION("Kattis second add"){
    		t.push_middle(1);
    		REQUIRE(t.get(1) == 5);
    		REQUIRE(t.get(2) == 1);

    		//added tests
			std::vector<int> v{3,5,1,9};
    		REQUIRE (t.size() == 4);
    		REQUIRE (t.to_vector() == v);
    		
    	}
    }
}

TEST_CASE("More special tests"){
	Teque t; 
	REQUIRE (t.size() == 0);
    REQUIRE (t.to_vector().size() == 0);

    SECTION("Variety"){
    	t.push_front(1);
    	t.push_back(2);
    	t.push_back(3);
    	t.push_middle(4);
    	t.push_back(5);
    	t.push_middle(6);


    	std::vector<int> v{1,2,4,6,3,5};
    	REQUIRE (t.size() == 6);
    	REQUIRE (t.to_vector() == v);
    }
    SECTION("Quantity Back"){
    	int n = 1000000; //max allowed
    	for (int i = 0; i < n; ++i)
    	{
    		t.push_back(i);
    	}
    	REQUIRE (t.size() == n);
    	for (int i = 0; i < n; ++i){
    		REQUIRE(t.get(i) == i);
    	}
    }
    SECTION("Quantity Front"){
    	int n = 1000000; //max allowed
    	for (int i = 0; i < n; ++i)
    	{
    		t.push_front(i);
    	}
    	REQUIRE (t.size() == n);
    	for (int i = n-1; i < 0; --i){
    		REQUIRE(t.get(i) == i);
    	}
    }
    SECTION("Quantity Middle"){
    	int n = 1000000; //max allowed
    	for (int i = 0; i < n; ++i)
    	{
    		t.push_middle(i);
    	}
    	REQUIRE (t.size() == n);
    }

}