const DELAY = 1500;

const createMockEndpoint = function(resolveValue: any, rejectValue: any, isResolved?: boolean): Promise<any> {
  return new Promise(function (resolve, reject) {
    setTimeout(function() {
      if (isResolved) {
        resolve(resolveValue);
      } else {
        reject(rejectValue);
      }
    }, DELAY);
  });
}

const getUserInfo = function(isResolved?: boolean) {
  return createMockEndpoint({ 
    name: 'Sanchoman', 
    inGame: false
  }, {
    message: 'No user with the provided token'
  }, 
  isResolved);
}

export { getUserInfo }