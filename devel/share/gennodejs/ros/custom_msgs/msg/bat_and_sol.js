// Auto-generated. Do not edit!

// (in-package custom_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class bat_and_sol {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.batStatus = null;
      this.solStatus = null;
      this.runtime = null;
      this.voltage = null;
      this.battery_percentage = null;
    }
    else {
      if (initObj.hasOwnProperty('batStatus')) {
        this.batStatus = initObj.batStatus
      }
      else {
        this.batStatus = '';
      }
      if (initObj.hasOwnProperty('solStatus')) {
        this.solStatus = initObj.solStatus
      }
      else {
        this.solStatus = '';
      }
      if (initObj.hasOwnProperty('runtime')) {
        this.runtime = initObj.runtime
      }
      else {
        this.runtime = '';
      }
      if (initObj.hasOwnProperty('voltage')) {
        this.voltage = initObj.voltage
      }
      else {
        this.voltage = 0.0;
      }
      if (initObj.hasOwnProperty('battery_percentage')) {
        this.battery_percentage = initObj.battery_percentage
      }
      else {
        this.battery_percentage = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type bat_and_sol
    // Serialize message field [batStatus]
    bufferOffset = _serializer.string(obj.batStatus, buffer, bufferOffset);
    // Serialize message field [solStatus]
    bufferOffset = _serializer.string(obj.solStatus, buffer, bufferOffset);
    // Serialize message field [runtime]
    bufferOffset = _serializer.string(obj.runtime, buffer, bufferOffset);
    // Serialize message field [voltage]
    bufferOffset = _serializer.float32(obj.voltage, buffer, bufferOffset);
    // Serialize message field [battery_percentage]
    bufferOffset = _serializer.float32(obj.battery_percentage, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type bat_and_sol
    let len;
    let data = new bat_and_sol(null);
    // Deserialize message field [batStatus]
    data.batStatus = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [solStatus]
    data.solStatus = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [runtime]
    data.runtime = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [voltage]
    data.voltage = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [battery_percentage]
    data.battery_percentage = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.batStatus.length;
    length += object.solStatus.length;
    length += object.runtime.length;
    return length + 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msgs/bat_and_sol';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5782c79eb06aac24e86dd4fe43a05d5f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string batStatus
    string solStatus
    string runtime
    float32 voltage
    float32 battery_percentage
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new bat_and_sol(null);
    if (msg.batStatus !== undefined) {
      resolved.batStatus = msg.batStatus;
    }
    else {
      resolved.batStatus = ''
    }

    if (msg.solStatus !== undefined) {
      resolved.solStatus = msg.solStatus;
    }
    else {
      resolved.solStatus = ''
    }

    if (msg.runtime !== undefined) {
      resolved.runtime = msg.runtime;
    }
    else {
      resolved.runtime = ''
    }

    if (msg.voltage !== undefined) {
      resolved.voltage = msg.voltage;
    }
    else {
      resolved.voltage = 0.0
    }

    if (msg.battery_percentage !== undefined) {
      resolved.battery_percentage = msg.battery_percentage;
    }
    else {
      resolved.battery_percentage = 0.0
    }

    return resolved;
    }
};

module.exports = bat_and_sol;
