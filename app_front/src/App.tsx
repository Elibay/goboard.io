import React from 'react';
import { withCookies, Cookies } from 'react-cookie';
import { PacmanLoader } from 'react-spinners';
import { MainPage } from './components';
import { getUserInfo } from './utils/mockApi';
import styled from 'styled-components';

const DELTA: number = 200;

interface IProps {
  cookies: Cookies;
}

interface IState {
  value: number;
  multiply: number;
  fetching: boolean;
  userInfo: any;
  gameMode: boolean;
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
      multiply: 1,
      fetching: true,
      userInfo: null,
      gameMode: false
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

    const token = this.props.cookies.get('token');

    if (token) {
      //const socket = new WebSocket('url');
      // getUserInfo(true)
      //   .then(userInfo => {
      //     this.setState({
      //       userInfo,
      //       fetching: false
      //     });
      //   })
      //   .catch(error => {
      //     console.log(error);
      //     this.setState({
      //       fetching: false
      //     });
      //   });
      
      
      this.setState({
        fetching: false
      });
    } else {
      this.setState({
        fetching: false
      });
    }
  }

  componentWillUnmount() {
    clearInterval(this.timer);
  }

  render() {
    const { fetching, gameMode } = this.state;

    let content = (
      <PacmanLoader
        sizeUnit='px'
        size={30}
        color='#f0f002'
      />
    );

    if (!fetching) {
      if (gameMode) {
        content = <p>Krauch, salam! Go and play!</p>;
      } else {
        content = <MainPage />;
      }
    }

    return (
      <Wrapper value={this.state.value}>
        {content}
      </Wrapper>
    );
  }
}

export default withCookies(App);
