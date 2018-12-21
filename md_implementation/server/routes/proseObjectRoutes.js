const proseObjectCtrl = require('../controllers/proseObject.ctrl.js');
const multipart = require('connect-multiparty');
const multipartWare = multipart();

module.exports = (router) => {
  // Gets a light version objects. Called at load.
  router
    .route('/objects')
    .get(proseObjectCtrl.getObjects)

  router
    .route('/object/:id')
    .get(proseObjectCtrl.getObjectId)
    .post(proseObjectCtrl.editObjectId)
    .delete(proseObjectCtrl.deleteObjectId)
}