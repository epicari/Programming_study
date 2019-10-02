/*
[문제2] 다음의 class를 완성 및 추가 class를 작성하여 문자열을 입력하는 Application을 작성하세요.
처리조건
- word processor는 body와 textBoxs(textBox의 집합)으로 구성된다.
- body와 textBox는 paragraphs(paragraph의 집합)으로 구성된다.
- 효율적인 메모리 관리를 위해서 paragraph의 text 메모리를 capacity 단위로 할당한다. 
- textPosition의 현재 설정된 위치에 문자열을 입력한다.
- textPosition의 textBoxIndex가 –1이면 body의 paragraph에 입력하고, 0 이상이면 해당 textBox의 paragraph에 입력한다.
- textBoxIndex나 paragraphIndex가 범위를 넘겨서 설정되면 해당 instance를 추가 할당한 후 입력한다.
- textOffset이 범위를 넘겨서 설정되면 입력이 실패하도록 한다.
- 실행 결과body의 첫 번째 paragraph = “aaaaabbbbbccccc” 두 번째 textBox의 두 번째 paragraph = “aabbcccccbbbaaa”
*/

#include<iostream>
#include<string>

using namespace std;

struct TextPosition {
	int textBoxIndex;
	unsigned int paragraphIndex;
	unsigned int textOffset;
};

class Paragraph {
public:
	static const int CAPACITY_UNIT = 20; // 효율적인 메모리 관리를 위해서 paragraph의 text 메모리를 capacity 단위로 할당한다.

	bool AddText(const TextPosition& textPosition, const std::string& text);

private:
	std::string text;
};

class Application {
public:
	TextPosition& GetTextPosition();

	virtual bool AddText(const std::string& text) = 0;

protected:
	TextPosition textPosition;
};

class WordProcessor : public Application {
public:
	virtual bool AddText(const std::string& text);

private:
	// body 선언
	// textBoxs 선언
};

int main(int argc, char* argv[])
{
	WordProcessor wordProcessor;
	TextPosition& textPosition = wordProcessor.GetTextPosition();

	wordProcessor.AddText("ccccc");
	wordProcessor.AddText("bbbbb");
	wordProcessor.AddText("aaaaa");

	textPosition.textBoxIndex = 1;
	textPosition.paragraphIndex = 1;
	textPosition.textOffset = 0;
	wordProcessor.AddText("aaaaa");

	textPosition.textOffset = 2;
	wordProcessor.AddText("bbbbb");

	textPosition.textOffset = 4;
	wordProcessor.AddText("ccccc");

	return 0;
}

// 실행 결과body의 첫 번째 paragraph = “aaaaabbbbbccccc” 두 번째 textBox의 두 번째 paragraph = “aabbcccccbbbaaa”