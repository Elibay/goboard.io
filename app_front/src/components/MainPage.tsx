import React, { useState } from 'react';
import { Input } from './';
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

const MainPage: React.FC = () => {
  const [isCreate, changeCreate] = useState(false);
  const [gameName, changeGameName] = useState('');
  const [pin, changePin] = useState('');

  const handleJoin = function() {
      
  }

  const toggleCreate = function() {
    changeCreate(!isCreate);
  }

  const handleStartGame = function() {
    
  }

  const form: React.ReactNode = isCreate ?
    (
      <>
        <Input
          placeholder="Name" 
          value={gameName} 
          onChange={event => changeGameName(event.target.value)} 
        />
        <Button onClick={handleStartGame}>
          Start!
        </Button>
        <Button onClick={toggleCreate}>
          Back
        </Button>
      </>
    ) :
    (
      <>
        <Input
          placeholder="Game PIN" 
          value={pin} 
          onChange={event => changePin(event.target.value)} 
        />
        <Button onClick={handleJoin}>
          Join
        </Button>
        <Button onClick={toggleCreate}>
          Create
        </Button>
      </>
    ); 

  return (
    <Page>
      <Header>
        Krarauch!
      </Header>
      {form}
    </Page>
  );
}   

export default MainPage;