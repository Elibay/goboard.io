import React, { useState } from 'react';
import styled from 'styled-components';

const Page = styled.div`
  text-align: center;
`;

const Header = styled.p`
  font-size: 75px;
  font-weight: bold;
  color: white;
  padding: 0;
  margin: 0;
`;

interface ButtonProps {
  create?: boolean;
}

const Button = styled.button<ButtonProps>`
  border: none;
  outline: none;
  font-size: 22px;
  font-weight: bold;
  display: block;
  margin: 0 auto;
  width: 220px;
  padding: 10px 30px;
  margin-top: ${props => props.create ? '35px' : '15px'};
  background-color: ${props => props.create ? '#1168ce' : 'rgb(51,51,51)'};
  color: white;
  border: 2px solid ${props => props.create ? '#1168ce' : '#2e2e2e'};

  &:hover {
    cursor: pointer;
  }
`;

const PinInput = styled.input`
  text-align: center;
  border: none;
  border: 2px solid #cccccc;
  font-size: 22px;
  font-weight: bold;
  padding: 10px 10px;
  width: 200px;
  margin-top: 30px;
`;

const MainPage: React.FC = () => {
  const [isJoin, changeJoin] = useState(false); 
  const [pin, changePin] = useState('');

  return (
    <Page>
      <Header>
        Krarauch!
      </Header>
      <PinInput
        placeholder="Game PIN" 
        value={pin} 
        onChange={event => changePin(event.target.value)} 
      />
      <Button onClick={() => changeJoin(true)}>
        Join
      </Button>
      <Button create>
        Create
      </Button>
    </Page>
  );
}   

export default MainPage;