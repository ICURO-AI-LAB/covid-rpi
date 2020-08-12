// Auto-generated. Do not edit!

// (in-package sanitation_control.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class trigger_textRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type trigger_textRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type trigger_textRequest
    let len;
    let data = new trigger_textRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'sanitation_control/trigger_textRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new trigger_textRequest(null);
    return resolved;
    }
};

class trigger_textResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.succeeded = null;
      this.message = null;
    }
    else {
      if (initObj.hasOwnProperty('succeeded')) {
        this.succeeded = initObj.succeeded
      }
      else {
        this.succeeded = false;
      }
      if (initObj.hasOwnProperty('message')) {
        this.message = initObj.message
      }
      else {
        this.message = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type trigger_textResponse
    // Serialize message field [succeeded]
    bufferOffset = _serializer.bool(obj.succeeded, buffer, bufferOffset);
    // Serialize message field [message]
    bufferOffset = _serializer.string(obj.message, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type trigger_textResponse
    let len;
    let data = new trigger_textResponse(null);
    // Deserialize message field [succeeded]
    data.succeeded = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [message]
    data.message = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.message.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'sanitation_control/trigger_textResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '92f07022ad10c1e4ff936618bca1e212';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool succeeded
    string message
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new trigger_textResponse(null);
    if (msg.succeeded !== undefined) {
      resolved.succeeded = msg.succeeded;
    }
    else {
      resolved.succeeded = false
    }

    if (msg.message !== undefined) {
      resolved.message = msg.message;
    }
    else {
      resolved.message = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: trigger_textRequest,
  Response: trigger_textResponse,
  md5sum() { return '92f07022ad10c1e4ff936618bca1e212'; },
  datatype() { return 'sanitation_control/trigger_text'; }
};
