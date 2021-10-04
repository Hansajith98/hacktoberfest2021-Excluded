const API_URL = 'https://api.quotable.io/random';
const TWEET_API_URL = 'https://twitter.com/intent/tweet';
const COLORS = [
  '#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3',
  '#03A9F4', '#00BCD4', '#009688', '#4CAF50', '#8BC34A', '#CDDC39',
  '#FFC107', '#FF9800', '#FF5722', '#795548', '#9E9E9E', '#607D8B',
];

const chooseRandom = (list) => {
  const index = Math.floor(Math.random() * list.length);
  return list[index];
}

const buildTweetURL = ({ author, text }) =>
  `${TWEET_API_URL}?hashtags=quotes&text="${text}" ${author}`;

const Button = ({ children, id, color, onClick, style, href }) => {
  const customStyle = { backgroundColor: color, ...style };
  return (
    <a
      id={id}
      className="button"
      onClick={onClick}
      style={customStyle}
      href={href /* required to pass tests */}
      target="_blank"
    >
      {children}
    </a>
  );
};


const QuoteBox = ({ color, text, author, onNewQuote, onTweetQuote }) => (
  <div id="quote-box" style={{ color }}>
    <div id="text">
      {text}
    </div>
    <div id="author">{author}</div>
    <div id="buttons-bar">
      <Button
        id="tweet-quote"
        onClick={onTweetQuote}
        color={color}
        href={buildTweetURL({ author, text })}
      >
        <i className="fa fa-fw fa-twitter" />
      </Button>
      <Button
        id="new-quote"
        onClick={onNewQuote}
        color={color}
        style={{ marginLeft: 'auto' }}
      >
        New quote
      </Button>
    </div>
  </div>
);

class App extends React.Component {
  state = {
    bgColor: '',
    quote: {
      text: null,
      author: null,
    }
  }

  componentDidMount = () => {
    this.fetchNewQuote();
  }

  fetchNewQuote = () => {
    this.chooseRandomBgColor();
    fetch(API_URL)
      .then((response) => response.json())
      .then((data) => {
        const quote = {
          author: data.author,
          text: data.content,
        };
        this.setState({ quote });
      });
  }

  chooseRandomBgColor = () => {
    const bgColor = chooseRandom(COLORS);
    this.setState({ bgColor });
  }

  tweetQuote = () => {
    const { quote } = this.state;
    const url = buildTweetURL(quote);
    window.open(url, '_blank');
  }

  render() {
    const bgColor = this.state.bgColor || 'black';

    return (
      <div
        id="quote-container"
        style={{ backgroundColor: bgColor }}
      >
        <QuoteBox
          color={bgColor}
          text={this.state.quote.text}
          author={this.state.quote.author}
          onNewQuote={this.fetchNewQuote}
          onTweetQuote={this.tweetQuote}
        />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));