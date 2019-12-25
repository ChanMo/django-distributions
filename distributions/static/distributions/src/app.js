import React from 'react';
import ReactDOM from 'react-dom';
import { Download } from 'react-feather'
import styled from 'styled-components'

const Wrapper = styled.div`
  background-image: url(${props => props.bg});
  background-size: 100% 100%;
  background-repeat: no-repeat;
  background-position: top center;
  text-align: center;
  padding: 4rem 2rem 0;
  width: 720px;
  max-width: 100%;
  box-sizing: border-box;
  margin: 0 auto;
`

const Logo = styled.img`
  border-radius: 3px;
  width: 120px;
  height: 120px;
  border-radius: 5px;
`

const Button = styled.a`
  margin-top: 4rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%);
  text-decoration: none;
  border-radius: 3px;
  box-shadow: 0 3px 5px 2px rgba(255, 105, 135, .3);
  color: white;
  height: 48px;
  padding: 0 30px;
  span {
    margin-left: .5rem;
  }
`

const VersionName = styled.p`
  font-size: 0.75rem;
  color: #b2bec3;
`

const Title = styled.h2`
  color: #2d3436;
`

const Desc = styled.p`
  font-size: 0.85rem;
  color: #636e72;
  line-height: 1.25rem;
`

const ModalImg = styled.div`
  position: fixed;
  top: 0;
  right: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0,0,0,.5);
  background-image: url(/static/distribution/wx.png);
  background-position: top right;
  background-repeat: no-repeat;
  background-size: 80vw 80vw;
`

const Modal = () => {
  const ua = navigator.userAgent.toLowerCase();
  if (ua.match(/MicroMessenger/i) != "micromessenger") {
    return null
  }
  return (
    <ModalImg />
  )
}

const App = () => (
  <Wrapper bg={props.bg}>
    <Modal />
    <Logo src={props.icon} alt={props.name} />
    <VersionName>版本v{props.version_name}</VersionName>
    <Title>{props.name}</Title>
    <Desc>{props.description}</Desc>
    <Button href={props.link}>
      <Download />
      <span>立即下载</span>
    </Button>
  </Wrapper>
);

ReactDOM.render(<App {...window.props}/>, document.getElementById('root'));
