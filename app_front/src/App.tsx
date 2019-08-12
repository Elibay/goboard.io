import React from 'react';
import { CookiesProvider } from 'react-cookie';
import { MainPage } from './components';
import styled from 'styled-components';

const DELTA: number = 200;

interface IProps {}

interface IState {
  value: number;
  multiply: number;
}

interface WrapperProps {
  value: number;
}

const Wrapper = styled.div<WrapperProps>`
  background-color: ${props => `rgba(230, 20, ${props.value}, 0.7)`};
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
`;

class App extends React.Component<IProps, IState> {
  private timer: any;

  constructor(props: IProps) {
    super(props);

    this.state = {
      value: 0,
      multiply: 1
    };
  }

  componentDidMount() {
    this.timer = setInterval(() => {
      this.setState(prevState => {
        const newValue = prevState.value + 5 * prevState.multiply;
        let newMultiply = prevState.multiply;

        if (newValue === 255 || newValue === 0) {
          newMultiply *= -1;
        }

        return {
          value: newValue,
          multiply: newMultiply
        }
      });
    }, DELTA);
  }

  componentWillUnmount() {
    clearInterval(this.timer);
  }

  render() {
    return (
      <CookiesProvider>
        <Wrapper value={this.state.value}>
          <MainPage />
        </Wrapper>
      </CookiesProvider>
    );
  }
}

export default App;
