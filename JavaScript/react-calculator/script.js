// ~ Calculator logic ~
const MAX_PROMPT_LENGTH = 10;
const MAX_HISTORY_LENGTH = 18;

const isPoint = key => key === '.';
const isZero = key => key === '0';
const isDigit = key => '0123456789'.indexOf(key) >= 0;
const isOp = key => '+-×÷'.indexOf(key) >= 0;
const isEqual = key => key === '=';
const isAC = key => key === 'AC';

const calcResult = ({ prompt, history }) => {
  let expr = `${history}${prompt}`;
  expr = expr.replace('÷', '/');
  expr = expr.replace('×', '*');
  const result = eval(expr);
  return result.toString().substr(0, 10);
};

const nextMode = (state, key) => {
  if (isAC(key)) return 'START';

  const { mode } = state;
  switch (mode) {
    case 'RESULT':
      if (isZero(key))
        return 'START';
      if (isDigit(key) || isPoint(key))
        return 'ACC';
      if (isOp(key))
        return 'OP';
      break;
    case 'START':
      if ((!isZero(key) && isDigit(key)) ||
        isPoint(key))
        return 'ACC';
      if (isOp(key))
        return 'OP';
      break;
    case 'ACC':
      if (isOp(key))
        return 'OP';
      if (isEqual(key))
        return 'RESULT';
      break;
    case 'OP':
      if ((!isZero(key) && isDigit(key)) ||
        isPoint(key))
        return 'ACC';
      break;
  }
  return mode;
};
const nextPrompt = (state, key) => {
  if (isAC(key)) return '0';

  const { mode, prompt, history } = state;
  switch (mode) {
    case 'RESULT':
      if (isDigit(key) || isOp(key))
        return key;
      if (isPoint(key))
        return '0.';
      break;
    case 'START':
    case 'OP':
      if ((!isZero(key) && isDigit(key)) ||
        isOp(key))
        return key;
      if (isPoint(key))
        return '0.';
      break;
    case 'ACC':
      if (isDigit(key) ||
        (isPoint(key) && prompt.indexOf('.') < 0))
        return `${prompt}${key}`.substr(0, MAX_PROMPT_LENGTH);
      if (isOp(key))
        return key;
      if (isEqual(key))
        return calcResult(state).substr(0, MAX_PROMPT_LENGTH);
      break;
  }
  return prompt;
};
const nextHistory = (state, key) => {
  if (isAC(key)) return '';

  const { mode, prompt, history } = state;
  switch (mode) {
    case 'RESULT':
      if (isDigit(key) || isPoint(key))
        return '';
      if (isOp(key))
        return prompt;
      break;
    case 'START':
      if (isPoint(key))
        return '';
      if (isOp(key))
        return `${history}${prompt}`;
      break;
    case 'OP':
      if ((!isZero(key) && isDigit(key)) ||
        isPoint(key))
        return `${history}${prompt}`;
      break;
    case 'ACC':
      if (isOp(key))
        return `${history}${prompt}`;
      if (isEqual(key))
        return `${history}${prompt}=`;
      break;
  }
  return history;
};

const digitsNames = ['one', 'two', 'three', 'four', 'five',
  'six', 'seven', 'eight', 'nine'];

// ~ Components ~

const CalculatorKey = ({ onKeyPress, keyName, id }) => {
  return (
    <div
      className="key"
      onClick={() => onKeyPress(keyName)}
    >
      <span id={id}>
        {keyName}
      </span>
    </div>
  );
}

const CalculatorKeys = ({ onKeyPress }) => {
  return (
    <div id="keys">
      {digitsNames.map((name, i) => (
        <div key={name} style={{
          gridRow: 4 - Math.floor(i / 3),
          gridColumn: 1 + i % 3
        }}>
          <CalculatorKey keyName={(i + 1).toString()}
            id={name} onKeyPress={onKeyPress} />
        </div>
      ))}
      <div style={{ gridRow: 5, gridColumn: "1 / span 2" }}>
        <CalculatorKey keyName="0" id="zero"
          onKeyPress={onKeyPress} />
      </div>
      <div style={{ gridRow: 5, gridColumn: 3 }}>
        <CalculatorKey keyName="." id="decimal"
          onKeyPress={onKeyPress} />
      </div>
      <div style={{ gridRow: "4 / span 2", gridColumn: 4 }}>
        <CalculatorKey keyName="=" id="equals"
          onKeyPress={onKeyPress} />
      </div>
      <div style={{ gridRow: 3, gridColumn: 4 }}>
        <CalculatorKey keyName="+" id="add"
          onKeyPress={onKeyPress} />
      </div>
      <div style={{ gridRow: 2, gridColumn: 4 }}>
        <CalculatorKey keyName="-" id="subtract"
          onKeyPress={onKeyPress} />
      </div>
      <div style={{ gridRow: 1, gridColumn: 4 }}>
        <CalculatorKey keyName="×" id="multiply"
          onKeyPress={onKeyPress} />
      </div>
      <div style={{ gridRow: 1, gridColumn: 3 }}>
        <CalculatorKey keyName="÷" id="divide"
          onKeyPress={onKeyPress} />
      </div>
      <div style={{ gridRow: 1, gridColumn: "1 / span 2" }}>
        <CalculatorKey keyName="AC" id="clear"
          onKeyPress={onKeyPress} />
      </div>
    </div>
  );
}

const CalculatorDisplay = ({ history, prompt }) => {
  let displayHistory = `${history}${prompt}`;
  if (displayHistory.length > MAX_HISTORY_LENGTH)
    displayHistory =
      '...' +
      displayHistory.substr(
        displayHistory.length - MAX_HISTORY_LENGTH,
        displayHistory.length
      );

  return (
    <div id="screen">
      <span id="display">{prompt}</span>
      <span id="history">{displayHistory}</span>
    </div>
  );
};

class Calculator extends React.Component {
  state = {
    mode: 'START', // START, ACC, OP, RESULT
    prompt: '0',
    history: '',
  }

  handleKeyPress = (key) => {
    const mode = nextMode(this.state, key);
    const prompt = nextPrompt(this.state, key);
    const history = nextHistory(this.state, key);
    this.setState({ mode, prompt, history });
  }

  render() {
    return (
      <div id="calculator">
        <CalculatorDisplay
          prompt={this.state.prompt}
          history={this.state.history}
        />
        <CalculatorKeys onKeyPress={this.handleKeyPress} />
      </div>
    );
  }
}

const App = () => <Calculator />
ReactDOM.render(<App />, document.getElementById('app'));